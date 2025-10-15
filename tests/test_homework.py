"""Autograding script."""
import os
from homework import homework   # 👈 importa tu módulo

def test_01():
    """Test word count job."""

    # 👇 ejecuta la función principal antes de comprobar los archivos
    homework.main()

    assert os.path.exists("files/output/summary.csv")
    assert os.path.exists("files/plots/top10_drivers.png")
