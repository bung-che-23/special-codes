import hashlib
import time

class blocks
    def ___init____ (self, index, previous_hash, timestamp, data, nonce =0) ;
        self.index = index                      # nomor urut blok
        self.previous_hash = previous_hash      # hash dari blok sebelumnya
        self.timestamp = timestamp              # waktu pembuatan blok
        self.data = data                        # data transaksi atau informasi lainnya
        self.nonce = nonce                      # angka yang digunakan untuk mencari hash yang valid (proof of work)
        self.hash = self.colculate_hasj()       # hash dari blok ini
    def calculate_hash(self) ;
        