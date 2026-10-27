# Maintainer: Pavlo Kilko Rødseth <pavlo@kilko.name>

pkgname=ttf-kibernetyk-mono
pkgver=1.0.1
pkgrel=4
pkgdesc='Geometric monospace typeface inspired by the Ukrainian Cybernetics School.'
arch=(any)
url='https://github.com/PavloKilko/KibernetykMono'
license=(custom:OFL)
# source=("https://github.com/PavloKilko/KibernetykMono/releases/download/v$pkgver/KibernetykMono-v$pkgver.zip")
source=("$pkgname-$pkgver.zip::https://github.com/PavloKilko/KibernetykMono/releases/download/v$pkgver/KibernetykMono-v$pkgver.zip")
b2sums=('SKIP')

package() {
  # install fonts/ttf -type f -name '*.ttf' -exec install -Dm644 -t "$pkgdir/usr/share/fonts/TTF" {} \;
  install -Dm644 -t "$pkgdir/usr/share/fonts/TTF" KibernetykMono/*.ttf
  install -Dm644 KibernetykMono/OFL.txt "$pkgdir/usr/share/licenses/$pkgname/OFL.txt"
}
