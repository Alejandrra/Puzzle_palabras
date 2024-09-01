from django.shortcuts import render
from .models import WordPuzzle
from django.shortcuts import render, get_object_or_404
import random

def generate_puzzle_grid(words, size):
    # Crear una cuadrícula vacía
    grid = [['' for _ in range(size)] for _ in range(size)]
    
    # Colocar las palabras en la cuadrícula
    for word in words:
        word = word.upper()
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])
            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
                if all(grid[row][col+i] in ('', word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col+i] = word[i]
                    placed = True
            elif direction == 'vertical':
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)
                if all(grid[row+i][col] in ('', word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row+i][col] = word[i]
                    placed = True
            elif direction == 'diagonal':
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - len(word))
                if all(grid[row+i][col+i] in ('', word[i]) for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row+i][col+i] = word[i]
                    placed = True

    # Rellenar las celdas vacías con letras aleatorias
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(size):
        for j in range(size):
            if grid[i][j] == '':
                grid[i][j] = random.choice(alphabet)
    
    return grid

def puzzle_view(request, puzzle_id):
    puzzle = get_object_or_404(WordPuzzle, id=puzzle_id)
    words = [word.strip() for word in puzzle.words.split(',')]
    grid = generate_puzzle_grid(words, puzzle.grid_size)
    return render(request, 'puzzle.html', {'puzzle': puzzle, 'grid': grid})

