def person(**detail):
    print(f"""
          My name is {detail['name']}.
          I am {detail['age']} years old. 
          I live in  {detail['address']}""")

person(name="Ram", age="12", address = "Kathmandu")