import time
import os

slide1 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
             $$$$$$$  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$        $          $$$$$$$  $$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$      $$$$$$$       $$$$$$$  $$$$$$$$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$      $$$$$$$     $$$        $$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$        $                  $$$$$$$$$$$$$$$$$$ 
  $$$$$$$$$$$$$$$$$$$$$$$$$$                   $      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            $$$$$ $$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
              $$$          $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
slide2 = """
                                       $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
                   $  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
               $$$$$$$$$$$$$                   $$$$$$$  $$$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$    $$$$$$$$        $$$$$$$  $$$$$$$$$$$$$$$$$$
           $$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$                             $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$       $$                  $$$$$$$$$$$$$$$$$$ 
        $$$$$$$$$$$$$$$$$$$$         $$$              $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$          $$$$$$      $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$                  $$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
           $$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
              $$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
                    $$$    $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
i = 3

while i >= 0:
    # очищаем окно терминала
    os.system('cls')
    # выводим сообщение
    print(slide1, end='\r')
    # засыпаем на 1 секунду
    time.sleep(1)

    # повторяем операцию для остальных строк
    os.system('cls')
    print(slide2, end='\r')
    time.sleep(1)
    i -= 1