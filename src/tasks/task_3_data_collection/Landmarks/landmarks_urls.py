import pickle
#https://www.destguides.com/en/itineraries/egypt/egypt-landmarks-famous-landmarks-egypt
#26 Famous Egyptian Landmarks
landmarks = []
#The Egyptian Museum
landmarks.append(("Egyptian Museum",
"https://www.google.com/search?q=The+Egyptian+Museum&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-7aneuJP2AhXngP0HHUicBrkQ_AUoAXoECAEQAw&biw=1403&bih=671&dpr=1.25"
))
#Giza Necropolis and Pyramids
landmarks.append(("Giza-Necropolis-and-Pyramids",
"https://www.google.com/search?q=Giza+Necropolis+and+Pyramids+&tbm=isch&ved=2ahUKEwiFtIqVuZP2AhUKtBQKHbHaDzAQ2-cCegQIABAA&oq=Giza+Necropolis+and+Pyramids+&gs_lcp=CgNpbWcQA1DYBViLDGD9EGgAcAB4AIABgQGIAeIGkgEDMC43mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=J-kUYsWEDYroUrG1v4AD&bih=671&biw=1403"
))
#Mosque of Muhammad Ali
landmarks.append(("Mosque-Muhammad-Ali",
"https://www.google.com/search?q=mosque+of+muhammad+ali+photos&tbm=isch&ved=2ahUKEwidrN6-xZP2AhUEBMAKHT1IA5IQ2-cCegQIABAA&oq=Mosque+of+Muhammad+Ali&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEAUQHjIGCAAQBRAeOgQIABBDOgQIABAYUKIHWIjyAmDwlgNoQnAAeB2AAb4BiAH0W5IBBTE2Ljk4mAEAoAEBqgELZ3dzLXdpei1pbWewAQDAAQE&sclient=img&ei=E_YUYt3WMISIgAa9kI2QCQ&bih=671&biw=1403"
))
#Khan el-Khalili
landmarks.append(("Khan el-Khalili",
"https://www.google.com/search?q=Khan+el-Khalili+photos&tbm=isch&ved=2ahUKEwiD-5v4xZP2AhXDWMAKHcbRAzQQ2-cCegQIABAA&oq=Khan+el-Khalili+photos&gs_lcp=CgNpbWcQAzIFCAAQgAQ6BAgAEEM6BggAEAcQHjoHCAAQsQMQQ1DpBljXG2D1L2gAcAB4AIABiQGIAfMQkgEEMC4xOJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=jPYUYoOFFcOxgQbGo4-gAw&bih=671&biw=1403"
))
#Abu Simbel Temples
landmarks.append(("Abu-Simbel-Temples",
"https://www.google.com/search?q=Abu+Simbel+Temples+photos&tbm=isch&ved=2ahUKEwj--puKxpP2AhUCtyoKHRtfB1QQ2-cCegQIABAA&oq=Abu+Simbel+Temples+photos&gs_lcp=CgNpbWcQAzoECAAQQzoGCAAQBxAeOgcIABCxAxBDOgUIABCABFCUBljHHmDAIGgAcAB4AIABnQGIAZMNkgEEMC4xM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=svYUYv7ZBYLuqgGbvp2gBQ&bih=671&biw=1403"
))
#St. Catherine's Monastery
landmarks.append(("St-Catherines-Monastery",
"https://www.google.com/search?q=St.+Catherine%27s+Monastery+photos&tbm=isch&ved=2ahUKEwiBrdKjxpP2AhWK7qQKHW1-BoEQ2-cCegQIABAA&oq=St.+Catherine%27s+Monastery+photos&gs_lcp=CgNpbWcQAzoHCAAQsQMQQzoFCAAQgAQ6BAgAEENQpApYmSJg5iloAHAAeACAAZ0BiAHHD5IBBDAuMTaYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=5_YUYsGdGYrdkwXt_JmICA&bih=671&biw=1403"
))
#Valley of the Kings
landmarks.append(("Valley of the Kings",
"https://www.google.com/search?q=Valley+of+the+Kings+photos&tbm=isch&ved=2ahUKEwjGq_KxxpP2AhVxQUEAHTFbCqEQ2-cCegQIABAA&oq=Valley+of+the+Kings+photos&gs_lcp=CgNpbWcQAzIFCAAQgAQ6BAgAEEM6BwgAELEDEEM6BggAEAcQHjoICAAQCBAHEB5Q9AVYsvwBYNr_AWgBcAB4AYABrQGIAcpdkgEFMC4xMDCYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=BfcUYoaVEvGChbIPsbapiAo&bih=671&biw=1403"
))
#Citadel of Qaitbay
landmarks.append(("Qaitbay-Citadel",
"https://www.google.com/search?q=Citadel+of+Qaitbay+photos&tbm=isch&ved=2ahUKEwiG94LNxpP2AhVWsSoKHe43CbYQ2-cCegQIABAA&oq=Citadel+of+Qaitbay+photos&gs_lcp=CgNpbWcQA1DNBlizFGCqHmgAcAB4AYABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=PvcUYobgC9biqgHu76SwCw&bih=671&biw=1403"
))
#Temple of Seti I
landmarks.append(("Temple-Seti-I",
"https://www.google.com/search?q=Temple+of+Seti+I+photos&tbm=isch&ved=2ahUKEwjfjofexpP2AhVHQ8AKHZIpBL8Q2-cCegQIABAA&oq=Temple+of+Seti+I+photos&gs_lcp=CgNpbWcQA1C_BliJGWDiHmgAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=YfcUYp_aN8eGgQaS05D4Cw&bih=671&biw=1403"
))
#Temple of Philae
landmarks.append(("Temple-Philae",
"https://www.google.com/search?q=Temple+of+Philae+photos&tbm=isch&ved=2ahUKEwj3tbyAx5P2AhXcAGMBHQ3RB8sQ2-cCegQIABAA&oq=Temple+of+Philae+photos&gs_lcp=CgNpbWcQA1DjBliHDmCrFWgAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=qvcUYve4BdyBjLsPjaKf2Aw&bih=671&biw=1403"
))
#Saqqara Necropolis
landmarks.append(("Saqqara-Necropolis",
"https://www.google.com/search?q=Saqqara+Necropolis+photos&tbm=isch&ved=2ahUKEwin2ICGx5P2AhVDjqQKHbJNDXcQ2-cCegQIABAA&oq=Saqqara+Necropolis+photos&gs_lcp=CgNpbWcQA1CFB1iIFGDtIWgAcAB4AYABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=tfcUYuepKsOckgWym7W4Bw&bih=671&biw=1403"
))
#Luxor Temple
landmarks.append(("Luxor-Temple",
"https://www.google.com/search?q=Luxor+Temple+photos&tbm=isch&ved=2ahUKEwik0ryrx5P2AhVLuSoKHXtuCYkQ2-cCegQIABAA&oq=Luxor+Temple+photos&gs_lcp=CgNpbWcQA1DSBlj-FGCrHmgAcAB4AoABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=BPgUYqTAEMvyqgH73KXICA&bih=671&biw=1403"
))
#Montaza Palace and Royal Gardens
landmarks.append(("Montazah-Palace",
"https://www.google.com/search?q=Montaza+Palace++photos&tbm=isch&ved=2ahUKEwiwuvLQx5P2AhUG0YUKHQdQDSAQ2-cCegQIABAA&oq=Montaza+Palace++photos&gs_lcp=CgNpbWcQA1DPB1iwD2DSF2gAcAB4AoABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=UvgUYrDJLYailwSHoLWAAg&bih=671&biw=1403"
))
#The Temple of Karnak
landmarks.append(("Karnak-Temple",
"https://www.google.com/search?q=The+Temple+of+Karnak+photos&tbm=isch&ved=2ahUKEwjT2oThx5P2AhU5gv0HHdIrDzkQ2-cCegQIABAA&oq=The+Temple+of+Karnak+photos&gs_lcp=CgNpbWcQA1CPCFiOHWDeImgAcAB4AoABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=dPgUYtPQJLmE9u8P0te8yAM&bih=671&biw=1403"
))
#Great Sphinx of Giza
landmarks.append(("Great-Sphinx-Giza",
"https://www.google.com/search?q=Great+Sphinx+of+Giza+photos&tbm=isch&ved=2ahUKEwjyvZeDyJP2AhUMxuAKHZzgCSYQ2-cCegQIABAA&oq=Great+Sphinx+of+Giza+photos&gs_lcp=CgNpbWcQA1CkB1iyGWD3JWgAcAB4AYABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=vPgUYvLvDIyMgwecwaewAg&bih=671&biw=1403"
))
#Dendera Temple Complex
landmarks.append(("Dendra-Temple-Complex",
"https://www.google.com/search?q=+photosDendera+Temple+Complex&tbm=isch&ved=2ahUKEwjRsKqUyJP2AhVsk_0HHSnLDoEQ2-cCegQIABAA&oq=+photosDendera+Temple+Complex&gs_lcp=CgNpbWcQA1DlBliLHWD4OGgAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=4PgUYtHACuym9u8PqZa7iAg&bih=671&biw=1403"
))
#Nubian Museum
landmarks.append(("Nubian-Museum",
"https://www.google.com/search?q=Nubian+Museum+photos&tbm=isch&ved=2ahUKEwil05GmyJP2AhUt_CoKHQbcA74Q2-cCegQIABAA&oq=Nubian+Museum+photos&gs_lcp=CgNpbWcQA1AAWIE7YKZIaABwAHgAgAEAiAEAkgEAmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=BfkUYuW8H634qwGGuI_wCw&bih=671&biw=1403"
))
#Bibliotheca Alexandrina
landmarks.append(("Bibliotheca-Alexandrina",
"https://www.google.com/search?q=bibliotheca+library+alexandria&source=lnms&tbm=isch&sa=X&ved=2ahUKEwis58aao5P2AhVahP0HHTMcAqsQ_AUoAXoECAEQAw&biw=1403&bih=663&dpr=1.25"
))
#Serapeum and Pompey's Pillar
landmarks.append(("Serapeum-Pompeys-Pillar",
"https://www.google.com/search?q=Serapeum+and+Pompey%27s+Pillar+photos&tbm=isch&ved=2ahUKEwjNw_-5yJP2AhVix4sKHXthD58Q2-cCegQIABAA&oq=Serapeum+and+Pompey%27s+Pillar+photos&gs_lcp=CgNpbWcQA1DfBlitE2DPG2gAcAB4AYABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=L_kUYo3wCeKOrwT7wr34CQ&bih=671&biw=1403"
))
#Al-Azhar Park
landmarks.append(("Al-azhar-Park",
"https://www.google.com/search?q=Al-Azhar+Park+photos&tbm=isch&ved=2ahUKEwj21_PJyJP2AhUZR8AKHSFOCxAQ2-cCegQIABAA&oq=Al-Azhar+Park+photos&gs_lcp=CgNpbWcQA1CkB1i4G2DoJGgAcAB4AoABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=UPkUYvbvH5mOgQahnK2AAQ&bih=671&biw=1403"
))
#Mortuary Temple of Hatshepsut
landmarks.append(("Mortuary-Temple-o-Hatshepsut",
"https://www.google.com/search?q=+photos+Mortuary+Temple+of+Hatshepsut&tbm=isch&ved=2ahUKEwjPnqvXyJP2AhXxEmMBHdyoDy0Q2-cCegQIABAA&oq=+photos+Mortuary+Temple+of+Hatshepsut&gs_lcp=CgNpbWcQA1D5BVjjO2CQP2gAcAB4AYABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=bPkUYs-4KvGljLsP3NG-6AI&bih=671&biw=1403"
))
#Mortuary Temple of Amenhotep III
landmarks.append(("Mortuary-Temple-Amenhotep-III",
"https://www.google.com/search?q=Mortuary+Temple+of+Amenhotep+III+photos&tbm=isch&ved=2ahUKEwjB3sHnyJP2AhXE7rsIHfLoBhYQ2-cCegQIABAA&oq=Mortuary+Temple+of+Amenhotep+III+photos&gs_lcp=CgNpbWcQA1AAWIAbYIMjaABwAHgAgAEAiAEAkgEAmAEAoAEBqgELZ3dzLXdpei1pbWewAQDAAQE&sclient=img&ei=jvkUYsHfJcTd7_UP8tGbsAE&bih=671&biw=1403"
))
#Temple of Kom Ombo (Kom Ombo Temple)
landmarks.append(("Kom-Ombo-Temple",
"https://www.google.com/search?q=Kom+Ombo+Temple+photos&tbm=isch&ved=2ahUKEwiB-9D5yJP2AhU7hf0HHRTgBqUQ2-cCegQIABAA&oq=Kom+Ombo+Temple+photos&gs_lcp=CgNpbWcQA1DIB1i_GWDyHmgAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=tPkUYoHRJbuK9u8PlMCbqAo&bih=671&biw=1403"
))
#Mosque of Ibn Tulun
landmarks.append(("Mosque-of-Ibn-Tulun",
"https://www.google.com/search?q=Mosque+of+Ibn+Tulun+photos&tbm=isch&ved=2ahUKEwjKv4iRyZP2AhXK0YUKHc69CAEQ2-cCegQIABAA&oq=Mosque+of+Ibn+Tulun+photos&gs_lcp=CgNpbWcQA1CKBljwEmDqF2gAcAB4A4ABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=5fkUYoq5LsqjlwTO-6II&bih=671&biw=1403"
))
#Catacombs of Kom El Shoqafa
landmarks.append(("Catacombs-of-Kom-El-Shoqafa",
"https://www.google.com/search?q=Catacombs+of+Kom+El+Shoqafa+photos&tbm=isch&ved=2ahUKEwiYkeacyZP2AhUPxyoKHQGFAqsQ2-cCegQIABAA&oq=Catacombs+of+Kom+El+Shoqafa+photos&gs_lcp=CgNpbWcQA1DRCVjWHGC2IWgAcAB4AYABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=_vkUYpiaFo-OqwGBiorYCg&bih=671&biw=1403"
))
#Cairo Tower
landmarks.append(("Cairo-Tower",
"https://www.google.com/search?q=cairo+tower&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjD7pm8xZP2AhX8_rsIHQEwA_8Q_AUoAXoECAEQAw&biw=1403&bih=671&dpr=1.25"
))
# Qalawun Complex
landmarks.append(("Qalawun-Complex",
"https://www.google.com/search?q=Qalawun+Complex&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiHpYaWxZP2AhVpiv0HHfU_BwoQ_AUoAXoECAIQAw&biw=1403&bih=671&dpr=1.25"
))
#The Mosque if Imam Al-Husayn in Cairo
landmarks.append(("Mosque-Imam Al-Husayn-Cairo",
"https://www.google.com/search?q=The+Mosque+of+the+Imam+Al-Husayn+Cairo+photos&tbm=isch&ved=2ahUKEwim9taryZP2AhXIiFwKHW5KDhUQ2-cCegQIABAA&oq=The+Mosque+of+the+Imam+Al-Husayn+Cairo+photos&gs_lcp=CgNpbWcQA1CbB1if6AJg8fECaABwAHgDgAEAiAEAkgEAmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=HfoUYubzIsiR8gLulLmoAQ&bih=671&biw=1403"
))
#Archangel Michael Coptic Orthodox Church in Aswan
landmarks.append(("Archangel-Michael-Coptic-Orthodox-Church-Aswan",
"https://www.google.com/search?q=Archangel+Michael%27s+Coptic+Orthodox+in+Aswan+photos&tbm=isch&ved=2ahUKEwjN5ZWsypP2AhWUwyoKHc1JASkQ2-cCegQIABAA&oq=Archangel+Michael%27s+Coptic+Orthodox+in+Aswan+photos&gs_lcp=CgNpbWcQA1DwCljyJWCSQWgAcAB4AYABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=K_sUYo2kApSHqwHNk4XIAg&bih=671&biw=1403"
))
#Hanging Church in Cairo Egypt
landmarks.append(("Hanging-Church-Cairo",
"https://www.google.com/search?q=Hanging+Church+Egypt+photos&tbm=isch&ved=2ahUKEwjD0oPBypP2AhVLtKQKHZ2-Dl0Q2-cCegQIABAA&oq=Hanging+Church+Egypt+photos&gs_lcp=CgNpbWcQA1CRDFi-mAxgwJ4MaABwAHgDgAEAiAEAkgEAmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=VvsUYsPPL8vokgWd_broBQ&bih=671&biw=1403"
))
#Al Mu'izz Li Din Allah Street
landmarks.append(("Al-Mu'izz-Li-Din-Allah-Street",
"https://www.google.com/search?q=Al+Mu%27izz+Li-Din+Allah+street+photos&tbm=isch&ved=2ahUKEwiNnfWWzJP2AhWH44UKHZaaBLQQ2-cCegQIABAA&oq=Al+Mu%27izz+Li-Din+Allah+street+photos&gs_lcp=CgNpbWcQA1AAWABgzAZoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=F_0UYs21FIfHlwSWtZKgCw&bih=671&biw=1403"
))
#Al Hakim Mosque
landmarks.append(('Al-Hakim-Mosque',
"https://www.google.com/search?q=Al+Hakim+Mosque+photos&tbm=isch&ved=2ahUKEwjK5tekzJP2AhUJuKQKHbHJDQ4Q2-cCegQIABAA&oq=Al+Hakim+Mosque+photos&gs_lcp=CgNpbWcQAzIFCAAQgAQ6BggAEAcQHjoICAAQBxAFEB5Q_wlYlUJg_kZoAHAAeACAAYQBiAGXIZIBBDAuMziYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=NP0UYsr8DInwkgWxk7dw&bih=671&biw=1403"
))
#Sayeda Zainab
landmarks.append(('Sayeda-Zaiban-Mosque-Cairo',
"https://www.google.com/search?q=Sayeda+Zainab+Mosque+Cairo+photos&tbm=isch&ved=2ahUKEwiWmNmq1JP2AhUfi_0HHW28BRAQ2-cCegQIABAA&oq=Sayeda+Zainab+Mosque+Cairo+photos&gs_lcp=CgNpbWcQA1DsBFiKEmCWF2gAcAB4AIABd4gB-gWSAQMwLjeYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=pAUVYpa2Ep-W9u8P7fiWgAE&bih=671&biw=1403"
))
#Baron Palace
landmarks.append(("Baron-Palace",
"https://www.google.com/search?q=Baron+Palace+photos&tbm=isch&ved=2ahUKEwiutJ-z1JP2AhVug_0HHXajBskQ2-cCegQIABAA&oq=Baron+Palace+photos&gs_lcp=CgNpbWcQAzIGCAAQCBAeOggIABCABBCxAzoFCAAQgAQ6BggAEAcQHjoICAAQBxAFEB46CAgAEAgQBxAeUOQGWIlAYKBMaAFwAHgAgAF8iAGcIpIBBDIuMziYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=tgUVYq6BDu6G9u8P9saayAw&bih=671&biw=1403"
))
#Mosque of Amr Ibn El-Aas
landmarks.append(("Mosque-of-Amr-Ibn-El-Aas",
"https://www.google.com/search?q=Mosque+of+Amr+Ibn+El-Aas+photos&tbm=isch&ved=2ahUKEwjNg-Hj1JP2AhUDR8AKHaFhAQgQ2-cCegQIABAA&oq=Mosque+of+Amr+Ibn+El-Aas+photos&gs_lcp=CgNpbWcQAzoGCAAQCBAeOggIABAIEAcQHjoICAAQBxAFEB46BggAEAcQHjoECAAQQzoFCAAQgAQ6BwgAELEDEENQygZYtxxgtidoAHAAeACAAYMBiAG5DJIBBDAuMTSYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=GwYVYo2KO4OOgQahw4VA&bih=671&biw=1403"
))
#Cairo Citadel
landmarks.append(("Cairo-Citadel",
"https://www.google.com/search?q=Cairo+Citadel+photos&tbm=isch&ved=2ahUKEwjPh-ak1ZP2AhXDWMAKHcbRAzQQ2-cCegQIABAA&oq=Cairo+Citadel+photos&gs_lcp=CgNpbWcQAzIFCAAQgAQ6CAgAEIAEELEDOgYIABAHEB46CAgAEAgQBxAeUJEKWKI3YMw6aABwAHgBgAGyAYgB9SGSAQQwLjM3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=pAYVYs-lFsOxgQbGo4-gAw&bih=671&biw=1403"
))
#Cave Church
landmarks.append(("Cave-Church",
"https://www.google.com/search?q=Cave+Church+photos&tbm=isch&ved=2ahUKEwit2ufK1ZP2AhWUzioKHQq0CyIQ2-cCegQIABAA&oq=Cave+Church+photos&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BggAEAcQHjoECAAQQzoICAAQBxAFEB46CAgAEAgQBxAeUKgGWIwuYLc1aAFwAHgAgAGBAYgBqhWSAQQwLjI0mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=9AYVYq2QBZSdqwGK6K6QAg&bih=671&biw=1403"
))
#Temple of Edfu
landmarks.append(("Edfu-Temple",
"https://www.google.com/search?q=Temple+of+Edfu+photos&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj5w_nrhpX2AhWKxIUKHW4gBy4Q_AUoAXoECAEQAw&biw=1536&bih=754&dpr=1.25"
))
#

print(len(landmarks))
for site, url in landmarks:
    print('\n'+site)
    print('\n')
    print(url)

with open('landmarks_search_urls.txt', 'wb') as fm:
   pickle.dump(landmarks, fm)
   
#pickle_off = open ("landmarks_search_urls.txt", "rb")
#landmarks_list = pickle.load(pickle_off)