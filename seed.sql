INSERT INTO stores (store_name, url, post_code) VALUES (
    'The Surfboard Warehouse', 
    'https://www.thesurfboardwarehouse.com.au/',
    4567
),
(
    'Surfboard Empire',
    'http://www.surfboardempire.com.au/',
    4575
),
(
    'Beach Beat - Alex Heads',
    'https://beachbeat.com.au/',
    4572

),
(
    'Beach Beat - Coolum',
    'https://beachbeat.com.au/',
    4573

),
(
    'Beach Beat - Caloundra',
    'https://beachbeat.com.au/',
    4551

),
(
    'Sideways Noosa',
    'https://sideways.com.au/',
    4567
);

INSERT INTO shapers (shaper_name, url) VALUES (
    'JS Industries',
    'https://jsindustries.com/'
),
(
    'Channel Islands Surfboards',
    'https://shop-au.cisurfboards.com/'
),
(
    'Pyzel Surfboards',
    'https://pyzelsurf.com.au/'
);

INSERT INTO surfboards (shaper_id, model_name, model_type, min_wave_size, max_wave_size, wave_type, break_type, skill_level) VALUES (
    1,
    'Forget Me Not Step Up',
    'Step up / Semi Gun',
    8,
    15,
    'big wave',
    'all',
    'expert'    
);