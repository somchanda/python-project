import base64
# Convert text from string to byte
simple_text = "Hello from Chanda"
print("String text: ", end="")
print(simple_text)
byte_text = simple_text.encode('utf-8')
print("Byte text: ", end="")
print(byte_text)
print('============================\n')

# Convert from string to base64
s_text = "I'm from group sp15"
b_text = s_text.encode('utf-8')
base_text = base64.encodebytes(b_text)
print("String text: ", s_text)
print("Byte text: ", b_text)
print("Base64 text: ", base_text)