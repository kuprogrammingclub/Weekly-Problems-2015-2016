## Beginner 1 - Using Stacks
__Source__: http://bit.ly/1LBjcIy

#### <u>Problem</u>: Implement a stack with push and pop functions.

For those in 168, you won't be formally taught stacks until 268, so here's a
crash course!

Stacks are data structures that operate in a __LIFO__ manner. This stands for
__Last In, First Out__. The way I try to envision this is as a box:

```

This is an empty stack (the bottom of the box):


|                     |
|                     |
|                     |
|                     |
|_____________________|


This is after two 'push' operations:

|                     |
|                     |
|    [2nd Item In]    |
|    [1st Item In]    |
|_____________________|     

```

As we can see, there is no way to get the first item put into the box without
removing the second item first. If you think of a stack of books, this operates
in a similar way.

So that's your explanation of stacks! It's just a way to hold objects in a way
such that the last item inserted is always the first one out and you can only
see what's on the top of the stack.

Your goal is to implement a stack with *push* and *pop* functions. *Push* pushes
an item onto the top of a stack and we will implement *Pop* as a way to take the
top item off (permanently) and while returning the object you're removing.
An alternative to this is to also implement a *Peek* function. In this
implementation, we can have *Peek* used to return what value is at the top of the
stack without removing that object. In this implementation, *Pop* doesn't
necessarily have to return the object at the top of the stack, but can be
implemented in such a way if you know you'll want the value you're removing when
you pop the stack.

For more (detailed) information on stacks, check out the
[Wikipedia page](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)!
