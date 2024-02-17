import errorprop as ep

# Example usage:
pi = ep.ErrorProp(3.14)
r = ep.ErrorProp(420, 69)

print(r.value, r.error)
print(r)

x = r + r

print(x.value, x.error)
print(x)


