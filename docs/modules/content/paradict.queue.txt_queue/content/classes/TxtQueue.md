Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.queue.txt\_queue**
 
A FIFO queue for processing textual Paradict data

> **Classes:** &nbsp; [TxtQueue](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.txt_queue/content/classes/TxtQueue.md#class-txtqueue)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class TxtQueue
A FIFO queue for processing textual Paradict data

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|buffer|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [put](#put) &nbsp;&nbsp; [\_read](#_read)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## get
Generator for iteratively getting each line composing the
        textual data stored in the buffer.
        Note that lines yielded won't end with a newline '
' character



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## put
Store textual data in the buffer. This data will then be iteratively
        extracted by the 'get' method, line by line.
        Note: make sure that each line is ended with a newline '
' character



**Signature:** (self, s)





**Return Value:** None

[Back to Top](#module-overview)


## \_read
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



