from django.shortcuts import render
from django.http import HttpResponse
import boggle.generate_board.generate_board as gb

# Create your views here.
def index(request):
    boggle_letters = gb.generate_board(gb.classic_four_dice, 4)
    boggle_letters = [item for sublist in boggle_letters for item in sublist]

    context = {
        "boggle_letters": boggle_letters
    }

    return render(request, 'index.html', context=context)

def test(request):
    return HttpResponse("Test")