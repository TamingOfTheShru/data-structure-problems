/**
 * Write a function kthToLastNode() that takes an integer kk 
 * and the headNode of a singly-linked list, and returns the 
 * kkth to last node in the list.
 */

function LinkedListNode(value) {
	this.value = value;
	this.next = null;
}

var a = new LinkedListNode("Angel Food");
var b = new LinkedListNode("Bundt");
var c = new LinkedListNode("Cheese");
var d = new LinkedListNode("Devil's Food");
var e = new LinkedListNode("Eccles");

a.next = b;
b.next = c;
c.next = d;
d.next = e;

kthToLastNode(2, a); //O(n) time and O(1) space
//_kthToLastNode(2, a); //O(n) time and O(1) space

function kthToLastNode(k, head) {
	var listLength = 1;
	var currentNode = head;
	while (currentNode.next != null) {
		currentNode = currentNode.next;
		listLength++; //find length of list
	}

	var kth = listLength - k
	currentNode = head; //make currentNode head again
	for (var i = 0; i < kth; i++) { //traverse listLength-k, which is basically the kth node
		currentNode = currentNode.next;
	}
	console.log(currentNode);
	return currentNode;
}

//Second approach(stick method)
function _kthToLastNode(k, head) {

	var leftNode = head;
	var rightNode = head;

	// move rightNode to the kth node
	for (var i = 0; i < k - 1; i++) {
		rightNode = rightNode.next;
	}

	while (rightNode.next) {	//reserve a distance of k elements between left and right node
		leftNode = leftNode.next;
		rightNode = rightNode.next;
	}

	return leftNode;
}