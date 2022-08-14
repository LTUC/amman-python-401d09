Tree Intersection

Algo
1- Define a function that will take 2 trees

2- declare an empty list for output

3- Calling the pre-order method, so it will return a list 
of tree's elements

4- Declare an empty Hashtable with the size of
one of the trees elements

5- Loop through list 1 setting all elements to 
the Hashtable

6- Loop over the second list checking if the 
Hashtable has the element using contains

7 if contains return true then will append to the 
output list

8- return the output list.

```
function(bt1,btr2){
    function _walk(node1, node2){
        if not node1 or not node2:
            return
        
        if node1.value == node2.value:
            output.append(node1.value)

        _walk(node1.left, node2.left)
        _walk(node2.right, node2.right)

    _walk(bt1.root, bt2.root)
    return output
}
}
```