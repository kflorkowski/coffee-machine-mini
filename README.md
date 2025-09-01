# CoffeeMachine
This is an educational project developed for learning and practicing core Python programming skills. The program allows users to interact with a virtual coffee machine: order drinks, manage resources (like water, milk, coffee), process payments using virtual coins, and generate reports.

## Installation guide
This project does not require any external dependencies, it runs entirely with Python’s standard library.

1. Make sure you have Python 3.6 or higher installed.
2. Download CoffeMachine project.
3. Open a terminal and navigate to the project folder.
4. Run the script: `python main.py`

## Usage guide
After running the script, you will see: 
`Type 'y' to turn ON coffee machine.`

Once turned on, the machine will ask: 
`What would you like? (espresso/latte/cappuccino):`

At this point, you can type any of the commands listed below:

| Command                             | Description                                              |
|-------------------------------------|----------------------------------------------------------|
| `espresso` / `latte` / `cappuccino` | Order selected coffee type                               |
| `report`                            | Display current levels of water, milk, coffee, and money |
| `refill`                            | Refill all resources to their maximum capacity           |
| `off`                               | Turn off the machine                                     |

When you choose a coffee type:

1. The machine checks if there are enough resources.
   - If not, it notifies you which ingredients are missing and returns to the main prompt.
   - If yes, it proceeds to the **payment stage**.

2. During payment:
   - You select a **coin type** (`quarter`, `dime`, `nickel`, `penny`).
   - Then specify the **number of coins** to insert.
   - The machine checks if the inserted amount is sufficient:
     - If **not enough**, it repeats the process.
     - If **enough**, it calculates change (if any) and brews the coffee.
     - If **invalid input**, it prompts you again.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.