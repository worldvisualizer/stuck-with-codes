-- this is a single-line comment
--[[

    this is a multi-line comment
]]--

-- 1. variables and control flows

num = 42 -- 64 bit int, 52-precision for number expression
s = 'walterwhite'
t = "this is also walterwhite"
u = [[ multiline string
       walter white impersonation
       and language flows through ]]
t = nil -- undefines t, lua has garbage collection

print(a, t, u)

while num < 50 do
  num = num + 1 -- no ++ or += type operator
end

if num > 40 then
  print('over 40')
elseif s ~= 'walterwhite' then
  io.write('not over 40\n')
else
  thisIsGlobal = 5 -- variables are global by default
  local line = io.read()
  print('winter is coming,' .. line)
  -- string concatenation uses .. operator
end

-- this is not an error. undefined vars return nil
foo = anUnknownVariable -- foo = nil

aBoolValue = false

-- only nil and false are falsy; 0 and '' are true
if not aBoolValue then print('oneline!') end

ans = aBoolValue and 'yes' or 'no'

karlSum = 0
for i = 1, 100 do
  karlSum = karlSum + 1
end

-- counting down
fredSum = 0
for j = 100, 1, -1 do fredSum = fredSum + j end

repeat
  print('this is the next while')
  num = num - 1
until num == 0

-- 2. functions

function fib(n)
  if n < 2 then return 1 end
  return fib(n-2) + fib(n-1)
end

-- closures and anonymous functions are there:
function adder(x)
  return function (y)
    x = x + 1
    return x + y
  end
end

a1 = adder(9)
a2 = adder(36)
print(a1(16))
print(a1(26))
print(a2(64))

-- returns, function calls, and assignments as well:
x, y, z = 1,2,3,4 -- 4 is thrown away

function bar(a, b, c)
  print(a,b,c)
  return 4,8,15,16,23,42
end

x, y = bar('zaphod') -- oh god

-- functions are first-class, and therefore local/global
function f(x) return x * x end
f = function (x) return x * x end
-- these two are same

-- and those are same as well
local function g(x) return math.sin(x) end
local g; g = function (x) return math.sin(x) end


-- 3. Tables

t = { key1 = 'value', key2 = false }
-- string keys can use js-like dot notation
print(t.key1)
t.newKey = {}
t.key2 = nil

-- literal notation for any (non-nil) value as key:
u = {['@!#'] = 'qbert', [{}] = 1729, [6.28] = 'tau'}
print(u[6.28]) -- "tau"

a = u['@!#']
b = u[{}] -- it's a nil, because the lookup fails
-- because it's not the same object reference. :(

function h(x) print(x.key1) end
h{key1 = 'Sonmi-431'}

for key, val in pairs(u) do -- this is table iteration
  print(key, val)
end

-- _G is a special table of all globals.
print(_G['_G'] == _G) -- this is true. what the fuck. ah. namespace.

v = {'value1', 'value2', 1.21, 'gigawatts'} -- this is a list
for i = 1, #v do -- #v is the size of v for lists
  print(v[i])
end

-- 3.1 metatables and metamethods

--[[
a table can have a metatable that gives the table
operator-overload ish behavior. 
--]] 


f1 = {a = 1, b = 2}
f2 = {a = 2, b = 3}

metafraction = {}
function metafraction._add(f1 ,f2)
  sum = {}
  sum.b = f1.b * f2.b
  sum.a = f1.a * f2.b + f2.a * f1.b
  return sum
end

setmetatable(f1, metafraction)
setmetatable(f2, metafraction)

s = f1 + f2 -- calls __add(f1, f2) on f1's metatable

defaultFavs = {animal = 'gru', food = 'donuts'}
myFavs = {food = 'pizza'}
setmetatable(myFavs, {__index = defaultFavs})
eatenBy = myFavs.animal

-- an __index on a metatable overloads dot lookups.
defaultFavs = {animal = 'gru', food = 'donuts'}
myFavs = {food = 'pizza'}
setmetatable(myFavs, {__index = defaultFavs})
eatenBy = myFavs.animal

-- direct table lookups that fail will retry using
-- the metatable's __index value, and this recurses.

-- an __index value can also be a function(tbl, key)
-- for more customized lookups.

-- values of __index, add, .. are called metamethods

-- __add(a, b)                     for a + b
-- __sub(a, b)                     for a - b
-- __mul(a, b)                     for a * b
-- __div(a, b)                     for a / b
-- __mod(a, b)                     for a % b
-- __pow(a, b)                     for a ^ b
-- __unm(a)                        for -a
-- __concat(a, b)                  for a .. b
-- __len(a)                        for #a
-- __eq(a, b)                      for a == b
-- __lt(a, b)                      for a < b
-- __le(a, b)                      for a <= b
-- __index(a, b)  <fn or a table>  for a.b
-- __newindex(a, b, c)             for a.b = c
-- __call(a, ...)                  for a(...)

-- 3.2 Class-like tables and inheritance

-- classes aren't builtin, instead use metatable.

Dog = {}

function Dog:new() -- this is a handmade constructor
  newObj = {sound = 'woof'}
  self.__index = self
  return setmetatable(newObj, self)
end

function Dog:makeSound()
  print('I say ' .. self.sound)
end

mrDog = Dog:new()
mrDog:makeSound() -- 'I say woof'

--[[
Dog acts like a class, and it's a table
function tablename:fn(...) is same as function tablename.fn(self, ...)
the : adds a first arg called self.
newObj will be an instance of class Dog
self = the class being instantiated. Often self = Dog, but inheritance can change it
newObj gets self's functions when we set both __index and metatable of newObj
setmetatable returns its first arg
]]--

LoudDog = Dog:new()

function LoudDog:makeSound()
  s = self.sound .. ' '
  print(s .. s .. s)
end

seymour = LoudDog:new()
seymour:makeSound()

--[[
1. LoudDog gets Dog's methods and variables.
2. self has a 'sound' key from new().
3. Same as LoudDog.new(LoudDog), and converted to Dog.new(LoudDog) as LoudDog has no 'new' key
4. the 'makeSound' key is found in LoudDog; this is the same as LoudDog.makeSound(seymour)
]]--

-- if needed, a subclass's new() is like the base's.
function LoudDog:new()
  newObj = {}
  -- set up newObj
  self.__index = self
  return setmetatable(newObj, self)
end

-- 4. Modules

-- file mod.lua can look like this.
local M = {}
local function sayMyName()
  print('Hrunker')
end

function M.sayHello()
  print('Hello there')
  sayMyName()
end

return M

-- another file can use mod.lua's functionalities:
-- require is the way to import module.
local mod = require('mod')

-- require acts like this. like mod.lua is a function body,
-- so that locals inside mod.lua are invisible outside it.
local mod = (function()
  --...
end)()

-- this works because mod here = M in mod.lua.
mod.sayHello()
mod.sayMyName()

-- require's return values are cached so a file is run at most once

-- suppose mod2.lua contains "print('Hi')"
local a = require('mod2')
local b = require('mod2') -- does not print hi

dofile('mod2.lua')
dofile('mod2.lua') -- prints hi again 

-- loadfile loads a lua file but doesn't run it yet
f = loadfile('mod2.lua') -- call f() to run it

-- loadstring is loadfile for strings
g = loadstring('print(343)') -- returns a function.
g() -- prints 343.


