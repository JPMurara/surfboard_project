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

INSERT INTO shapers (shaper_name, email, url, is_admin, password_hash) VALUES 
(
    'JS Industries',
    'jsindustries@email.com',
    'https://jsindustries.com/',
    true,
    'password_test'
),
(
    'Channel Island',
    'allmerick@email.com',
    'https://shop-au.cisurfboards.com/',
    true,
    'password_test'
),
(
    'Pyzel Surfboards',
    'pyzel@email.com',
    'https://pyzelsurf.com.au/',
    true,
    'password_test'
);


INSERT INTO surfboards (shaper_id, model_name, model_type, min_wave_size, max_wave_size, wave_type, break_type, skill_level, img_single, img_detail, url) VALUES 
(
    1,
    'Forget Me Not 3 Step Up',
    'Step Up / Semi Gun',
    8,
    15,
    'big wave',
    'all',
    'expert',
    'https://jsindustries.com/cdn/shop/files/forget-me-not-3-step-up-deck-jsindustries.jpg?v=1683256698&width=480',
    'https://jsindustries.com/cdn/shop/files/forget-me-not-3-step-up-jsindustries.jpg?v=1683256199&width=840',
    'https://jsindustries.com/products/copy-of-forget-me-not-ii-step-up'
),
(
    1,
    'Schooner',
    'Step Up / Semi Gun',
    2,
    8,
    'all',
    'all',
    'expert',
    'https://jsindustries.com/cdn/shop/products/schooner-deck-jsindustries-surfboards.jpg?v=1664419467&width=840',
    'https://jsindustries.com/cdn/shop/products/schooner-all-jsindustries-surfboards.jpg?v=1664419460&width=840',
    'https://jsindustries.com/products/schooner'
),
(
    1,
    'Forget Me Not 3',
    'High Performance',
    4,
    8,
    'powerful',
    'all',
    'intermediate',
    'https://jsindustries.com/cdn/shop/files/forget-me-not-3-deck-js-industries-surfboards.jpg?v=1683236414&width=480',
    'https://jsindustries.com/cdn/shop/files/forget-me-not-3-full-js-industries-surfboards.jpg?v=1682464226&width=840',
    'https://jsindustries.com/products/forget-me-not-3'
),
(
    1,
    'Monsta 10',
    'High Performance',
    3,
    6,
    'powerful',
    'all',
    'intermediate',
    'https://jsindustries.com/cdn/shop/products/monsta10-easyrider-deck-jsindustries-surfboards.jpg?v=1678920426&width=480',
    'https://jsindustries.com/cdn/shop/products/monsta10-easyrider-all-jsindustries-surfboards.jpg?v=1678920426&width=840',
    'https://jsindustries.com/products/monsta-10-easy-rider'
),
(
    1,
    'Black Baron',
    'Grovler',
    2,
    4,
    'mushy',
    'beach',
    'beginner',
    'https://jsindustries.com/cdn/shop/products/black-baron-deck-js-industries-surfboards_1_2.jpg?v=1680215661&width=840',
    'https://jsindustries.com/cdn/shop/products/black-baron-all-js-industries-surfboards.jpg?v=1660627430&width=840',
    'https://jsindustries.com/products/black-baron'
),
(   
    1,
    'Sub Xero',
    'Grovler',
    2,
    4,
    'mushy',
    'beach',
    'beginner',
    'https://jsindustries.com/cdn/shop/products/sub-xero-pu-deck-js-industries-surfboards.jpg?v=1680215600&width=840',
    'https://jsindustries.com/cdn/shop/products/sub-xero-pu-all-js-industries-surfboards.jpg?v=1664419373&width=840',
    'https://jsindustries.com/products/sub-xero'
),
(
    1,
    'Xero',
    'Daily Driver',
    2,
    4,
    'all',
    'beach',
    'intermediate',
    'https://jsindustries.com/cdn/shop/products/Xero-easy-rider-deck-js-industries-surfboards_2c756aee-cc8b-4bd3-bafd-578a5e119344.jpg?v=1680215618&width=480',
    'https://jsindustries.com/cdn/shop/products/Xero-easy-rider-all-js-industries-surfboards_6e46533c-29b4-41f6-b525-02cc5d01de42.jpg?v=1670797805&width=840',
    'https://jsindustries.com/products/xero'
),
(
    1,
    'Ranging Bull',
    'Daily Driver',
    2,
    8,
    'all',
    'all',
    'intermediate',
    'https://jsindustries.com/cdn/shop/products/raging-bull-deck.jpg?v=1680215552&width=840',
    'https://jsindustries.com/cdn/shop/products/raging-bull-all_1.jpg?v=1664419293&width=840',
    'https://jsindustries.com/products/raging-bull'
),
(
    2,
    'Happy Traveller',
    'Step Up / Semi Gun',
    6,
    12,
    'big wave',
    'all',
    'expert',
    'https://shop-au.cisurfboards.com/cdn/shop/products/Happy_Traveler_Deck_Web.png?v=1626910353',
    'https://shop-au.cisurfboards.com/cdn/shop/products/Happy_Traveler_Bottom_Web.png?v=1626910353',
    'https://shop-au.cisurfboards.com/products/happy-traveler-1'
),
(
    2,
    'Taco Grinder',
    'Step Up / Semi Gun',
    8,
    15,
    'big wave',
    'all',
    'expert',
    'https://shop-au.cisurfboards.com/cdn/shop/products/taco_grinder_deck1.png?v=1626910724',
    'https://shop-au.cisurfboards.com/cdn/shop/products/jordy_smith_taco_grinder_6.5x19.1.8x2.5.8.png?v=1626910724',
    'https://shop-au.cisurfboards.com/products/taco-grinder-1'
),
(
    2,
    'Rook 15',
    'High Performance',
    5,
    8,
    'powerful',
    'all',
    'expert',
    'https://shop-au.cisurfboards.com/cdn/shop/products/rookie_deck1.png?v=1626910749',
    'https://shop-au.cisurfboards.com/cdn/shop/products/Adriano-De-Souza-Rook15-59-x-18-3_16-x-2-1_8-Deck.png?v=1626910749',
    'https://shop-au.cisurfboards.com/products/rook-15'
),
(
    2,
    'CI Pro',
    'High Performance',
    4,
    8,
    'powerful',
    'all',
    'intermediate',
    'https://cisurfboards.com/cdn/shop/products/CI_Pro-Blue_Top.png?v=1663694995',
    'https://cisurfboards.com/cdn/shop/products/CI_Pro-Blue_Bottom.png?v=1663694995',
    'https://cisurfboards.com/products/ci-pro'
),
(
    2,
    'Biscuit Bonzer',
    'Groveler',
    2,
    4,
    'mushy',
    'beach',
    'beginner',
    'https://cisurfboards.com/cdn/shop/products/BonzerBiscuitBlueTop.png?v=1619469073',
    'https://cisurfboards.com/cdn/shop/products/BonzerBiscuitBlueBottom.png?v=1619469073',
    'https://cisurfboards.com/products/biscuit-bonzer'
),
(
    2,
    'Weirdo Ripper',
    'Groveler',
    3,
    4,
    'mushy',
    'beach',
    'beginner',
    'https://cisurfboards.com/cdn/shop/products/weirdo_ripper_deck.png?v=1619468545',
    'https://cisurfboards.com/cdn/shop/products/weirdo_ripper_bottom.png?v=1619468545',
    'https://cisurfboards.com/products/weirdo-ripper'
),
(
    2,
    'Rocket Wide',
    'Daily Driver',
    3,
    5,
    'all',
    'beach',
    'intermediate',
    'https://cisurfboards.com/cdn/shop/products/ROCKET-WIDE_Black-Rails_PU_Top.png?v=1619470518',
    'https://cisurfboards.com/cdn/shop/products/ROCKET-WIDE_Black-Rails_PU_Bottom.png?v=1619470518',
    'https://cisurfboards.com/products/rocket-wide'
),
(
    2,
    'OG Flyer',
    'Daily Driver',
    3,
    5,
    'all',
    'beach',
    'intermediate',
    'https://cisurfboards.com/cdn/shop/products/OG-Flyer-Deck-for-Web.png?v=1619470436',
    'https://cisurfboards.com/cdn/shop/products/OG-Flyer-Bottom-for-Web-700x2458.png?v=1619470436',
    'https://cisurfboards.com/products/og-flyer'
),
(
    3,
    'Ghost',
    'Step Up / Semi Gun',
    5,
    8,
    'big wave',
    'all',
    'expert',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-the-ghost_a_540x.jpg?v=1642637769',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-the-ghost_b_540x.jpg?v=1642637769',
    'https://pyzelsurf.com.au/products/ghost'
),
(
    3,
    'Tank',
    'Step Up / Semi Gun',
    8,
    15,
    'big wave',
    'all',
    'expert',
    'https://pyzelsurf.com.au/cdn/shop/products/Pyzel-Tank-1_360x.jpg?v=1643684645',
    'https://pyzelsurf.com.au/cdn/shop/products/Pyzel-Tank-2_360x.jpg?v=1643684645',
    'https://pyzelsurf.com.au/products/tank'
),
(
    3,
    'Shadow',
    'High Performance',
    4,
    6,
    'powerful',
    'all',
    'intermediate',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-the-shadow_a_360x.jpg?v=1642637836',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-the-shadow_b_360x.jpg?v=1642637836',
    'https://pyzelsurf.com.au/products/theshadow'
),
(
    3,
    'Radius',
    'High Performance',
    3,
    5,
    'powerful',
    'all',
    'intermediate',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-the-radius_a_360x.jpg?v=1642646085',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-the-radius_b_360x.jpg?v=1642646085',
    'https://pyzelsurf.com.au/products/radius'
),
(
    3,
    'Gremlin',
    'Groveler',
    2,
    4,
    'mushy',
    'beach',
    'beginner',
    'https://pyzelsurf.com.au/cdn/shop/products/Pyzel-Gremlin-1_360x.jpg?v=1643688811',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-gremlin_b_360x.jpg?v=1646175808',
    'https://pyzelsurf.com.au/products/gremlin'
),
(
    3,
    'Astro Pop',
    'Groveler',
    2,
    5,
    'mushy',
    'beach',
    'beginner',
    'https://pyzelsurf.com.au/cdn/shop/products/Pyzel-Astro-Pop-1_360x.jpg?v=1643685282',
    'https://pyzelsurf.com.au/cdn/shop/products/Pyzel-Astro-Pop-2_360x.jpg?v=1643685282',
    'https://pyzelsurf.com.au/products/astropop'
),
(
    3,
    'Pyzalien',
    'Daily Driver',
    3,
    6,
    'all',
    'all',
    'intermediate',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-pyzalien_a_360x.jpg?v=1646098473',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-pyzalien_b_360x.jpg?v=1646098473',
    'https://pyzelsurf.com.au/products/pyzalien'
),
(
    3,
    'Phantom',
    'Daily Driver',
    3,
    6,
    'all',
    'all',
    'intermediate',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-phantom_round_a_360x.jpg?v=1646101807',
    'https://pyzelsurf.com.au/cdn/shop/products/pyzel-phantom_round_b_360x.jpg?v=1646101807',
    'https://pyzelsurf.com.au/products/phantomround'
)