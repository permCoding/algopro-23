import g4f

def get_message(request):
    response = g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": request}],
        n=1,
        stream=True,
        provider=g4f.Provider.You
    )
    return response


request = "Выбери лишнее: блокнот, ручка, кошка, карандаш. Поясни свой выбор."
print(''.join([message for message in get_message(request)]))