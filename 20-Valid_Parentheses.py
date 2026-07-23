def validparen(s):
  stack = []
  p = {")":"(","}":"{","]":"["}
  for i in s:
    if i in p:
      if not stack or stack.pop() != p[i]:
        return False
    else:
      stack.append(i)
  return len(stack) == 0

a = "({[]})"
print(validparen(a))
