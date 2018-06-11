from conans import ConanFile

class LibConan(ConanFile):
    name = "lib"
    version = "1.0"
    exports_sources = "CMakeLists.txt"
 
    def build(self):
        from build import build_palmerita
        build_palmerita(self)

