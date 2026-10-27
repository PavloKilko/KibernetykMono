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
b2sums=('ed1086e311ce36488969315cc00641b0171e5242a758beff87f8c43ba534ccc1221319b8ce0dd9ba4f17e26a93453ab7fd195ca3d8430fafccd96a592ba7a9fb')

package() {
  # install fonts/ttf -type f -name '*.ttf' -exec install -Dm644 -t "$pkgdir/usr/share/fonts/TTF" {} \;
  install -Dm644 -t "$pkgdir/usr/share/fonts/TTF" KibernetykMono/*.ttf
  install -Dm644 KibernetykMono/OFL.txt "$pkgdir/usr/share/licenses/$pkgname/OFL.txt"
}
