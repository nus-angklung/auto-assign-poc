# [PoC] Autogenerate angklung assignment

## Up and Running

```python
pip3 install -r requirements.txt
```

To run:
```python
python3 main.py
```

## Docx requirement

Mostly based on how the Avengers.docx are set up

1. I expect there is a title for the song, because I will skip the first line
2. I expect the angklung parts to be annotated with "Ang."
3. I expect the sheets to be in a table format. Each crotchet (beat) is in its
   own cells. This should result in a 4D nested list representing the whole
   documents when parsed
4. I expect the bar numbers to only be in the first barline, because I will
   remove it afterwards
