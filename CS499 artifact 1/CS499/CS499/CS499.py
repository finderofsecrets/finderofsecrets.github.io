"""
This project is for CS499 - Computer Science Capstone. 
I am recreating a binary search tree from scratch in Python.
"""
import csv


# define the structure to hold bid information
class Bid:
    bidId: str
    title: str
    fund: str
    amount: float
    def __init__(self, bidId='', title='', fund='', amount=0.0):
        self.bidId = bidId
        self.title = title
        self.fund = fund
        self.amount = amount

# define the structure for a node in the binary search tree
class Node:
    bid: Bid
    left: 'Node'
    right: 'Node'
    def __init__(self, bid: Bid):
        self.bid = bid
        self.left = None
        self.right = None

#Define a binary search tree class with methods for inserting, searching, and traversing the tree.
class BinarySearchTree:
    root: Node
    def __init__(self):
        self.root = None

# define a method to display bid information
    @staticmethod
    def displayBid(bid: Bid):
        print(f"Bid ID: {bid.bidId}, Title: {bid.title}, Fund: {bid.fund}, Amount: ${bid.amount:.2f}")

# define traversal methods for the binary search tree
# in-order, post-order, and pre-order
    def inOrder(self):
        self._inOrderTraversal(self.root)

    def _inOrderTraversal(self, node: Node):
        if node is not None:
            self._inOrderTraversal(node.left)
            BinarySearchTree.displayBid(node.bid)
            self._inOrderTraversal(node.right)

    def postOrder(self):
        self._postOrderTransversal(self.root)

    def _postOrderTransversal(self, node: Node):
        if node is not None:
            self._postOrderTransversal(node.left)
            self._postOrderTransversal(node.right)
            BinarySearchTree.displayBid(node.bid)

    def preOrder(self):
        self._preOrderTraversal(self.root)

    def _preOrderTraversal(self, node: Node):
        if node is not None:
            BinarySearchTree.displayBid(node.bid)
            self._preOrderTraversal(node.left)
            self._preOrderTraversal(node.right)

# define methods for inserting, removing, and searching for bids in the binary search tree
    def insert(self, bid: Bid):
        if self.root is None:
            self.root = Node(bid)
        else:
            self._addNode(self.root, bid)

    def _addNode(self, node: Node, bid: Bid):
        if bid.bidId < node.bid.bidId:
            if node.left is None:
                node.left = Node(bid)
            else:
                self._addNode(node.left, bid)
        else:
            if node.right is None:
                node.right = Node(bid)
            else:
                self._addNode(node.right, bid)

    def remove(self, bidId: str):
        self.root = self._removeNode(self.root, bidId)

    def _removeNode(self, node: Node, bidId: str) -> Node | None:
        if node is None:
            return node
        if bidId < node.bid.bidId:
            node.left = self._removeNode(node.left, bidId)
        elif bidId > node.bid.bidId:
            node.right = self._removeNode(node.right, bidId)
        else:
            if (node.left is None) and (node.right is None):
                return None
            elif (node.left is not None ) and (node.right is None):
                temp = node.left
                return temp
            elif (node.left is None) and (node.right is not None):
                temp = node.right
                return temp
            else:
                temp = node.right
                while temp.left is not None:
                    temp = temp.left
                node.bid = temp.bid
                node.right = self._removeNode(node.right, temp.bid.bidId)
        return node

    def search(self, bidId: str) -> Bid | None:
        return self._searchNode(self.root, bidId)

    def _searchNode(self, node: Node, bidId: str) -> Bid | None:
        if node is None:
            return None
        if bidId == node.bid.bidId:
            return node.bid
        elif bidId < node.bid.bidId:
            return self._searchNode(node.left, bidId)
        else:
            return self._searchNode(node.right, bidId)

#main function to demonstrate the binary search tree functionality
def main():
    bst = BinarySearchTree()
    loaded = False #prevents accidental multiple loads

    choice: int = 0
    while choice !=9:
        print("Menu:")
        print("  1. Load Bids")
        print("  2. Display All Bids in Order")
        print("  3. Find Bid")
        print("  4. Remove Bid")
        print("  9. Exit")
        
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        match choice:
            case 1:
                if (loaded == False) :
                    with open('eBid_Monthly_Sales.csv', 'r') as csvfile:
                        bidReader = csv.reader(csvfile)
                        next(bidReader) # skip header
                        for row in bidReader:
                            bidId = row[1]
                            title = row[0]
                            fund = row[8]
                            amount = float(row[4].replace('$', '').replace(',', ''))
                            bid = Bid(bidId, title, fund, amount)
                            bst.insert(bid)
                    print("Bids loaded.")
                    loaded = True
                else:
                    print("Bids have already been loaded.")

            case 2:
                if bst.root is None:
                    print("No bids to display.")
                else:
                    bst.inOrder()
            case 3:
                bidId = input("Enter Bid ID to search: ")
                bid = bst.search(bidId)
                if bid is not None:
                    BinarySearchTree.displayBid(bid)
                else:
                    print("Bid not found.")
            case 4:
                bidId = input("Enter Bid ID to remove: ")
                bst.remove(bidId)
                print("Bid removed if it existed.")
            case 9:
                print("Exiting...")
            case _:
                print("Invalid choice. Please try again.")

# run the main function
if __name__ == "__main__":
    main()
    