CREATE OR REPLACE VIEW statistics as
SELECT '����� ������' as measure,
       COUNT(*) as value
FROM heroes
UNION ALL
SELECT '������ ������� ����� ������' as measure,
       COUNT(*) as value
FROM heroes h
WHERE h.side='SUN_CARCHA'
UNION ALL
SELECT '������ ������� ����� ����' as measure,
       COUNT(*) as value
FROM heroes h
WHERE h.side='SHADOW_CARCHA'
UNION ALL
SELECT '����� ��������' as measure,
       COUNT(*) as value
FROM battles b
UNION ALL
SELECT '����������� �� ������� ����� ������' as measure,
       COUNT(*) as value
FROM battles b
inner join heroes h1 on h1.id=b.hero_id_1
inner join heroes h2 on h2.id=b.hero_id_2
WHERE
      h1.side='SUN_CARCHA' AND b.winner=1 OR
      h2.side='SUN_CARCHA' AND b.winner=2
UNION ALL
SELECT '����������� �� ������� ����� ����' as measure,
       COUNT(*) as value
FROM battles b
inner join heroes h1 on h1.id=b.hero_id_1
inner join heroes h2 on h2.id=b.hero_id_2
WHERE
      h1.side='SHADOW_CARCHA' AND b.winner=1 OR
      h2.side='SHADOW_CARCHA' AND b.winner=2
UNION ALL
SELECT '����� ��������' as measure,
       COUNT(*) as value
FROM mottos m
UNION ALL
SELECT '�������� ������ ����� ������' as measure,
       COUNT(*) as value
FROM mottos m
INNER JOIN heroes h on m.hero_id = h.id
WHERE h.side='SUN_CARCHA'
UNION ALL
SELECT '�������� ������ ����� ����' as measure,
       COUNT(*) as value
FROM mottos m
INNER JOIN heroes h on m.hero_id = h.id
WHERE h.side='SHADOW_CARCHA'