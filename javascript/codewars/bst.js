function Node(value) {
  this.value = value;
  this.dups = 1;
  this.left = null;
  this.right = null;
};

class BSTDupe {
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
      if (rootnode.left === null) {
        rootnode.left = node;
      } else {
        this.insertRecursively(rootnode.left, node);
      }
    }
  }
}

function constructBSTDups(nums) {
  let answer = [];
  const bst = new BSTDupe();
  for (var i = 0; i < nums.length; i++) {
    const node = new Node(nums[i]);
    bst.insert(node);
  }
  console.log(bst.root);
  return bst;
}

// constructBSTDups([5,4,3,2,1]);
constructBSTDups([1,3,3,2]);
