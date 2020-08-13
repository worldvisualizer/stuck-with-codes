<!-- html programming possible, but markup syntax
not usable in the element -->

# this is an <h1>
## this is <h2>
### this is <h3>
#### this <h4>
##### this <h5>
###### this <h6>

This is also h1
================

This is an h2
----------------

*This is in italics*
_This also_

**This is in bold**
__This also__

***This is both!***
**_wtf_**
*__wtf2__*

--in github markdown, this is strikethrough--

paragraphs are a one or multiple adjacent lines of text separated by one or multiple blank lines. so this is paragraph 1.

this is paragraph2.
But this is still paragraph2.

Paragraph 3. newline huh?

Ending paragraph with two spaces or more can make spaces between paragraphs.    


> this is a block quote. awesome.
>> this is further indentation inside block quote

unordered lists can be made using these

* Item
* Item
* Another Item

or

+ Item
+ Item
+ One more time

or 

- Item
- My favorite way of creating list
- One last item

ordered list?

1. Item one
2. Item two
3. Item three
  * Sub-item fine
  * Sub-item fine

there are even task lists. this creates HTML checkboxes
- [ ] First task
- [ ] Second task
- [x] This task is completed

You can indicate a code block by indenting a line
with four spaces or a tab

    This is code
    this is also code

    my_array.each do |item|
        puts item
    end

Let's create inline code: `goto()` 

Github markdown

```ruby
def foobar
  puts "hello world"
end
```

Horizontal rules are:

***
---
- - -
****************

Links

[Caption (click me!)](https://seungwoo.jung.co)
[Click me!](http://test.com/ "Link to Test.com")
[Go to music](/music/).
[link1]: http://test.com/ "Cool!"
[foobar]: http://foobar.biz/ "Alright!"

Images

![This is alt-attribute][https://imgur.com/.... "optional title"]

Tables

Only seen in Github or Remarkup, but...
:--- is alignment

| Col1 | Col2     | Col3    |
| :--- | :------: | ------: |
| Left | Center   | Right   |
| bah  | blah     | blyat   |

