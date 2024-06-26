def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Superman", power="Fly")
print_kwargs(name="Spiderman", power="Net")
print_kwargs(name="Batman", Asset="Money")
