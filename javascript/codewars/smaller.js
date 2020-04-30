function Node(value) {
  this.value = value;
  this.leftSum = 0;
  this.dups = 1;
  this.left = null;
  this.right = null;
};

class BSTDupeSmaller {
  constructor() {
    this.root = null;
  }

  insert(node) {
    if (!this.root) {
      this.root = node;
    } else {
      this.insertRecursively(this.root, node);
    }
  }

  insertRecursively(rootnode, node) {
    if (rootnode.value < node.value) {
      if (rootnode.right === null) {
        rootnode.right = node;
      } else {
        this.insertRecursively(rootnode.right, node);
      }
    } else if (rootnode.value === node.value) {
      rootnode.dups += 1;
    } else {
      rootnode.leftSum += 1;
      if (rootnode.left === null) {
        rootnode.left = node;
      } else {
        this.insertRecursively(rootnode.left, node);
      }
    }
  }
}

function findSmaller(node, number, sumSofar) {
  if (node.value === number) {
    return sumSofar;
  } else if (node.value > number) {
    return findSmaller(node.left, number, node.leftSum + node.dups);
  } else {
    return findSmaller(node.right, number, node.leftSum + node.dups);
  }
}

function smaller(nums) {
  let answer = [];
  const bst = new BSTDupeSmaller();

  for (var i = 0; i < nums.length; i++) {
    const node = new Node(nums[i]);
    bst.insert(node);
  }
  console.log(bst.root);
  for (var i = 0; i < nums.length; i++) {
    answer.push(findSmaller(bst.root, nums[i], 0));
  }
  return answer;
}

function assertEquals(arr1, arr2) {
  const jarr1 = JSON.stringify(arr1);
  const jarr2 = JSON.stringify(arr2);
  console.log(`${jarr1 === jarr2}: Expected ${jarr2}, Got ${jarr1}`)
}

assertEquals(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0]);