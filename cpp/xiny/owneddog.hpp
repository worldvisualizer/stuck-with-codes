

void OwnedDog::setOwner(const std::string& dogsOwner) {
	owner = dogsOwner;
}

void OwnedDog::print() const {
	// super function
	Dog::print();
	std::cout << "This is owned by... " << owner;
}