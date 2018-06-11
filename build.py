from cpt.packager import ConanMultiPackager
from conans import CMake


def build_palmerita(conanfile):
    cmake = CMake(conanfile)
    cmake.configure()
    cmake.build()
    print("Palmerita")


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    builder.run()
