# https://codecombat.com/play/level/gems-or-death
# Команды, находящиеся в теле if-оператора, написанные ниже будут исполнятся только если условие будет выполнено.
# Исправьте все if-операторы для прохождения уровня.

# == значит "равно ли", т.е. сравнение.
if 1 + 1 + 1 == 30:  # ∆ Сделайте тут "false"
    hero.moveXY(5, 15)  # Идите к первой группе мин.

if 2 + 2 == 4:  # ∆ Сделайте тут "true"
	hero.moveXY(15, 40)  # Идите к первому самоцвету.

# != значит "не равно".
if 2 + 3 != 4:  # ∆ Сделайте тут "true"
	hero.moveXY(25, 15)  # Идите ко второму самоцвету.
	
# < значит "меньше чем".
if 2 + 2 < 5:  # ∆ Сделайте тут "true"
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)

if 2 < 0:  # ∆ Сделайте тут "false"
	hero.moveXY(40, 55)

if not True:  # ∆ Сделайте тут "false"
	hero.moveXY(50, 10)

if not False:  # ∆ Сделайте тут "true"
	hero.moveXY(55, 25)