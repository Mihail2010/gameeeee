import json

with open('game_j.json', 'r', encoding='utf-8') as f:
    game = json.load(f)

inventory = []
cur = game['start_node']

while True:
    node = game['nodes'][cur]
    print("\n" + "="*60)
    print(node['desc'])

    if node.get('is_end'):
        break

    opti = []
    for opt in node.get('opti', []):
        if 'condition' in opt:
            if 'has_item' in opt['condition']:
                if opt['condition']['has_item'] not in inventory:
                    continue
        opti.append(opt)


    if not opti and 'fallback_room6' in node and cur == 'room6':
        cur = node['fallback_room6']
        continue

    if not opti:
        print("\n[Тупик. Перезапусти игру]")
        break

    for i, opt in enumerate(opti, 1):
        print(f"{i}. {opt['text']}")

    while True:
        choice = int(input("\nТвой выбор: "))
        if 1 <= choice <= len(opti):
            break
        print(f"Введи число от 1 до {len(opti)}")

    selected = opti[choice-1]

    if 'action' in selected and selected['action'] == 'add_item':
        inventory.append(selected['item'])
        print(f"\n[Ты взял: {selected['item']}]")

    cur = selected['next']

print("\nИгра завершена!")
