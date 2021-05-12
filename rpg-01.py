class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        return "%s has %d health and %d power." % (self.name, self.health, self.power)


class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    # Hero attacks Goblin
    def attack(self, boss):
        boss.health -= sudri.power


class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    # Goblin attacks Hero
    def attack(self, hero):
        hero.health -= goblin.power


class Undead(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def attack(self, hero):
        hero.health -= self.power

    def alive(self):
        return True


sudri = Hero('Sudri', 40, 5)
goblin = Goblin('Goblin', 10, 4)
bone_crawler = Undead('Bone Crawler', 10, 2)


def main():

    while bone_crawler.alive() and sudri.alive():
        print(sudri.print_status())
        print(bone_crawler.print_status())
        print()
        print("What do you want to do?")
        print("1. fight boss")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            sudri.attack(bone_crawler)
            print("You do %d damage to the boss." % sudri.power)
            if bone_crawler.health <= 0:
                print("The goblin is dead.")

        elif user_input == "2":
            pass

        elif user_input == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid input %r" % user_input)

        if bone_crawler.health > 0:
            # Goblin attacks hero
            sudri.health -= bone_crawler.power
            print("The boss does %d damage to you." % bone_crawler.power)
            if sudri.health <= 0:
                print("You are dead.")


main()


# hero.attack(goblin)
# def __str__(self):
#     return self.name + ' is on a journey.'

# if goblin.health > 0:
#     # Goblin attacks hero
#     sudri.health -= goblin.power
#     print("The goblin does %d damage to you." % goblin.power)
#     if sudri.health <= 0:
#         print("You are dead.")

# sudri.attack(goblin)
# goblin.attack(sudri)
# sudri.is_alive()
# goblin.is_alive()
