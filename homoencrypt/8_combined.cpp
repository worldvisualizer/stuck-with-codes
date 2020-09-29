// Licensed under the MIT license.

#include "examples.h"

using namespace std;
using namespace seal;

void example_combined_test()
{
    print_example_banner("Example: HE Combined Test");

    /*
    In this example we demonstrate evaluating the following equation

        5 * (A^5) * (B^4)

    where A = 100 and B = 0.001.

    We start by setting up the CKKS scheme.
    */
    EncryptionParameters parms(scheme_type::CKKS);

    /*
    To keep the size of the intermediate results in check, we rearrange
    the equation to

        (5 * A) * ((A * B)^2)^2.

    We also see that the number of rescaling required is at most 4.
    To accomodate this, we choose 40, 36, 36, 36, 36, 24 for
    coeff_modulus. Better estimates can be probably acheived by
    tuning the numbers bit further. Also, the size of special prime
    may be a bit too small.
    */
    size_t poly_modulus_degree = 8192;
    parms.set_poly_modulus_degree(poly_modulus_degree);
    parms.set_coeff_modulus(CoeffModulus::Create(poly_modulus_degree, { 40, 36, 36, 36, 36, 24 }));

    double scale = pow(2.0, 36);

    auto context = SEALContext::Create(parms);
    print_parameters(context);
    cout << endl;

    KeyGenerator keygen(context);
    auto public_key = keygen.public_key();
    auto secret_key = keygen.secret_key();
    auto relin_keys = keygen.relin_keys_local();
    Encryptor encryptor(context, public_key);
    Evaluator evaluator(context);
    Decryptor decryptor(context, secret_key);

    CKKSEncoder encoder(context);

    Plaintext A_plain, B_plain, five_plain;
    encoder.encode(100, scale, A_plain);
    encoder.encode(0.001, scale, B_plain);
    encoder.encode(5, scale, five_plain);

    print_line(__LINE__);
    cout << "Encrypting A and B" << endl;
    Ciphertext A_encrypted;
    Ciphertext B_encrypted;
    encryptor.encrypt(A_plain, A_encrypted);
    encryptor.encrypt(B_plain, B_encrypted);
    cout << "   + Scale of A_encrypted: " << log2(A_encrypted.scale()) << " bits" << endl;
    cout << "   + Scale of B_encrypted: " << log2(B_encrypted.scale()) << " bits" << endl;
    cout << "   + Modulus chain index for A_encrypted: "
         << context->get_context_data(A_encrypted.parms_id())->chain_index() << endl;
    cout << endl;

    print_line(__LINE__);
    cout << "Multiplying A and B" << endl;
    Ciphertext AB_encrypted;
    evaluator.multiply(A_encrypted, B_encrypted, AB_encrypted);
    evaluator.relinearize_inplace(AB_encrypted, relin_keys);
    cout << "   + Scale of AB_encrypted before rescale: " << log2(AB_encrypted.scale()) << " bits" << endl;
    evaluator.rescale_to_next_inplace(AB_encrypted);
    cout << "   + Scale of AB_encrypted after rescale: " << log2(AB_encrypted.scale()) << " bits" << endl;
    cout << "   + Modulus chain index for AB_encrypted: "
         << context->get_context_data(AB_encrypted.parms_id())->chain_index() << endl;
    cout << endl;

    print_line(__LINE__);
    cout << "Square AB" << endl;
    Ciphertext AB_square_encrypted;
    evaluator.square(AB_encrypted, AB_square_encrypted);
    evaluator.relinearize_inplace(AB_square_encrypted, relin_keys);
    cout << "   + Scale of AB_square_encrypted before rescale: " << log2(AB_square_encrypted.scale()) << " bits" << endl;
    evaluator.rescale_to_next_inplace(AB_square_encrypted);
    cout << "   + Scale of AB_square_encrypted after rescale: " << log2(AB_square_encrypted.scale()) << " bits" << endl;
    cout << "   + Modulus chain index for AB_square_encrypted: "
         << context->get_context_data(AB_square_encrypted.parms_id())->chain_index() << endl;
    cout << endl;

    print_line(__LINE__);
    cout << "Square square of AB" << endl;
    Ciphertext AB_square_square_encrypted;
    evaluator.square(AB_square_encrypted, AB_square_square_encrypted);
    evaluator.relinearize_inplace(AB_square_square_encrypted, relin_keys);
    cout << "   + Scale of AB_square_square_encrypted before rescale: " << log2(AB_square_square_encrypted.scale()) << " bits" << endl;
    evaluator.rescale_to_next_inplace(AB_square_square_encrypted);
    cout << "   + Scale of AB_square_square_encrypted after rescale: " << log2(AB_square_square_encrypted.scale()) << " bits" << endl;
    cout << "   + Modulus chain index for AB_square_square_encrypted: "
         << context->get_context_data(AB_square_square_encrypted.parms_id())->chain_index() << endl;
    cout << endl;

    print_line(__LINE__);
    cout << "Multiply 5 by A" << endl;
    Ciphertext five_A_encrypted;
    evaluator.multiply_plain(A_encrypted, five_plain, five_A_encrypted);
    evaluator.relinearize_inplace(five_A_encrypted, relin_keys);
    cout << "   + Scale of five_A_encrypted before rescale: " << log2(five_A_encrypted.scale()) << " bits" << endl;
    evaluator.rescale_to_next_inplace(five_A_encrypted);
    cout << "   + Scale of five_A_encrypted after rescale: " << log2(five_A_encrypted.scale()) << " bits" << endl;
    cout << "   + Modulus chain index for five_A_encrypted: "
         << context->get_context_data(five_A_encrypted.parms_id())->chain_index() << endl;
    cout << endl;

    print_line(__LINE__);
    cout << "Mod switching of 5 times A" << endl;
    evaluator.mod_switch_to_next_inplace(five_A_encrypted);
    cout << "   + Scale of five_A_encrypted after first mod switch: " << log2(five_A_encrypted.scale()) << " bits" << endl;
    evaluator.mod_switch_to_next_inplace(five_A_encrypted);
    cout << "   + Scale of five_A_encrypted after second mod switch: " << log2(five_A_encrypted.scale()) << " bits" << endl;
    cout << "   + Modulus chain index for five_A_encrypted: "
         << context->get_context_data(five_A_encrypted.parms_id())->chain_index() << endl;
    cout << endl;

    print_line(__LINE__);
    cout << "Final multiplication of (AB^2)^2 and 5*A" << endl;
    Ciphertext result_encrypted;
    evaluator.multiply(AB_square_square_encrypted, five_A_encrypted, result_encrypted);
    evaluator.relinearize_inplace(result_encrypted, relin_keys);
    cout << "   + Scale of result_encrypted before rescale: " << log2(result_encrypted.scale()) << " bits" << endl;
    evaluator.rescale_to_next_inplace(result_encrypted);
    cout << "   + Scale of result_encrypted after rescale: " << log2(result_encrypted.scale()) << " bits" << endl;
    cout << "   + Modulus chain index for result_encrypted: "
         << context->get_context_data(result_encrypted.parms_id())->chain_index() << endl;
    cout << endl;

    print_line(__LINE__);
    cout << "Decrypting result" << endl;
    Plaintext plain_result;
    decryptor.decrypt(result_encrypted, plain_result);
    vector<double> result;
    encoder.decode(plain_result, result);
    print_vector(result, 3, 7);
}
