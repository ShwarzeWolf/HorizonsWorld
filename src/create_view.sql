CREATE OR REPLACE VIEW statistics as
SELECT 'Всего героев' as measure,
       COUNT(*) as value
FROM heroes
UNION ALL
SELECT 'Героев стороны Карха Солнца' as measure,
       COUNT(*) as value
FROM heroes h
WHERE h.side='SUN_CARCHA'
UNION ALL
SELECT 'Героев стороны Карха Тьмы' as measure,
       COUNT(*) as value
FROM heroes h
WHERE h.side='SHADOW_CARCHA'
UNION ALL
SELECT 'Всего сражений' as measure,
       COUNT(*) as value
FROM battles b
UNION ALL
SELECT 'Победителей со стороны Карха Солнца' as measure,
       COUNT(*) as value
FROM battles b
inner join heroes h1 on h1.id=b.hero_id_1
inner join heroes h2 on h2.id=b.hero_id_2
WHERE
      h1.side='SUN_CARCHA' AND b.winner=1 OR
      h2.side='SUN_CARCHA' AND b.winner=2
UNION ALL
SELECT 'Победителей со стороны Карха Тьмы' as measure,
       COUNT(*) as value
FROM battles b
inner join heroes h1 on h1.id=b.hero_id_1
inner join heroes h2 on h2.id=b.hero_id_2
WHERE
      h1.side='SHADOW_CARCHA' AND b.winner=1 OR
      h2.side='SHADOW_CARCHA' AND b.winner=2
UNION ALL
SELECT 'Всего слоганов' as measure,
       COUNT(*) as value
FROM mottos m
UNION ALL
SELECT 'Слоганов героев Карха Солнца' as measure,
       COUNT(*) as value
FROM mottos m
INNER JOIN heroes h on m.hero_id = h.id
WHERE h.side='SUN_CARCHA'
UNION ALL
SELECT 'Слоганов героев Карха Тьмы' as measure,
       COUNT(*) as value
FROM mottos m
INNER JOIN heroes h on m.hero_id = h.id
WHERE h.side='SHADOW_CARCHA'