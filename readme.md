# Horizons world
������ ������ - ��������� ��������� ���� Horizons: Zero Dawn. 
� ��� ������� ����� �������� ������, ���������� � ���, � ����� 
������������ �������� � ���������� �� ������.

## �������� ������
### ����� ���� ������
![img.png](schema.png)

### ��������
�������� �������:
- **�����:** id, �������, ���, �����, ���� ��������, ���� �����, �������, �� ������� �� ��������� - 
�� �������, ��� ��������� �� ���� �� ������� ����� ������. ��� �������� ������ �� ���� �������
������ � ������ ��������� ��������, ����� ������� ������������ 
- **������� ������:** id, hero_id, motto_id (��� ������� ����� ��������� ����������
� 0), ����� �������. � ������� ����� ����� ���� �� 1-�� �� ���������� �������� (����� 1 �� ������) 
- **������������ ������:** id, hero_1_id, hero_1_motto_id (= id ������� ��������), hero_2_id, hero_2_motto_id, 
winner (0 ��� ������, 1 ��� ����� 1, 2 ��� ����� 2). ����� 1 - ��������� �����.
- **������� ����������� ����� ��� ���������:** id, hero_id, story. 
1 ����� - ������ 1 �������. ��� ���������� ������� �����, � �������� ��� ���� �������, ������� 
����������������

## ������������� �������
 
������������ ������� ������� ����� � ������ **docker-compose.yml** �
**docker-compose.prod.yml** - ��� ���������� � ���������� ��������������.
� ��� ������������ ������ ����������� ��������� �� ������ **.env.dev** ��� **.env.prod**.
��� �������������, ��������� ������� ����� �������� ������ ���� ������.

����� ��������� ��������� ������� �������� � ����� **.env** � ����� src. � ������: 
- **�����** ��� �������� ��������-����� ���-��������� � ��� 
- **id ������ � ����������**, � ������� ��� ����� �� ��������� ������ ���� (�������� � ��� ����� �� ������ 
https://t.me/+tWkdPlHzos8yZTQ6)
- **������ �����������** ��� ���� ������, � ������� ����� �������� � ������ ����������� ��������� ������ �� 
������ .env.prod � .env.dev (��������,��� ������� �������� � �������� ����� IDE)

### development: docker
��� ���������� ����� ��������� ��������� ������� �� ����� �������:
```Linux Kernel Module
docker-compose up -d --build
```
� ���������� ���������� ������� ���������� 2 ����������: � ����� ������ postgres
� �� ������ python. ����������� ��� ����������� �����������, 
� ������ ���������� ������ �� �������� ���� ������ � ���������� �� �������.


### production: docker
��� ������� ������� �� ���������� ����� ��������� ��������� ������� �� ����� �������:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yml up -d --build
```

����� ���������� ����������, ������� �������:
```Linux Kernel Module
docker-compose -f docker-compose.prod.yml down -v
```

## ������ � ��������
����� ���� ��� ������ ������� (�������� ��� � ������), � ��� ����� ����������������� ����� ��������� ������. ��� ����� ���������� ������� 
� ����� src. � ��������� ����� ��������� ��������� �������:
**1. �������� ������� ��� ���� ��������:** 
```Linux Kernel Module
python -m scripts
```
**2. �������� ������� �� ���������� �������:** 
```Linux Kernel Module
python -m scripts [COMMAND] --help
```
**3. �������� ����� c ������������ ������:**
```Linux Kernel Module
python -m scripts add-hero NAME 
```
����� ����� ������� ��������� ���������: 
   - **--side** TEXT - �������, �� ������� ��������� �����. �� ������� ������ ��������� 
   �� ������� ����, �� ����� ������. ��������� ��������: SUN_CARCHA, SHADOW_CARCHA. ��������, �������� �� �����, �������
*NoSuchHeroSideException*
   - **--birthday** TEXT - ���� �������� ����� � ISO �������. ��� ��������, �������� �� �����, 
������� _IncorrectHeroBirthdayException_
   - **--tribe** TEXT - �����, � ������� ����� ��� ������
   - **--power** INTEGER  - ���� �����, ������� ������ �� ����������� ��� ������ (���� ������, ���� �� ������),
   �� �� � ������� ������� �����. ��������� �������� - 0

**4. �������� ����� ����� �������:** 
```Linux Kernel Module
python -m scripts add-battle
```

��� ���� �������� ���������� ������� � ����� �������, ������� � ������ 
�������, �� ������ � ����������. ������ ����������� � ������� battles

**5. �������� ����� ����� ��� ��������:** 
```Linux Kernel Module
python -m scripts add-motto HERO_ID TEXT
```
���� ������ ����� �� ����������, �� ������ ������ � ������� HeroNotFoundException

**7. �������� ����������� �����:** 
```Linux Kernel Module
python -m scripts add-story HERO_ID TEXT
```

���� ������ ����� �� ����������, �� ������ ������ � ������� HeroNotFoundException.
���� � ����� ��� ���������� ������, �� ������ �������������� ������������ ��������

**8. ������� �����:** 
```Linux Kernel Module
python -m scripts delete-hero HERO_ID
```
������� ����� �� ���� ������. ��� ���� �������� ��� ��� ������ ��� �������� � �����������.
���������� � ����� �������� � ���������. 
��� �������� � ������������ ������������� ���������� � ���, ����� �� �� ������� �����. ����� ������� ���� `--force`,
����� ������� �� ����.
���� ������ ����� �� ����������, �� ������ ������ �������������� � ���, ��� ������ ����� ���

**9. ������� ��� ���������� �� ���� ������:**
```Linux Kernel Module
python -m scripts database-dump
```
��������� ������, ����� ������� ��� �������� �� ���� ������ (��������, ��� �������� �������)

������ ����� � ������� ������� `python manage.py` ����� �������� ������, ��� �������� ���� ������ � ���������� �� 
��������� ������� � 6 ������, �� �������, ��������, � 10 �������� ��������.
**������������ �� ������������� ������������ ��� ������ �� ����� - ��� ������ ����� ������**
