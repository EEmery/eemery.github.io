Title: Making the KORG nanoKontrol More Colorful
Date: 2026-05-16 14:50
Lang: en
Slug: making-the-korg-nanokontrol-more-colorful
Translation: true

I've been working on a project that has several of these tiny servos, about 8, but with the possibility of increasing that number a bit. The project isn't complex, neither in hardware nor software. The problem is that sometimes, during the development process, I need to align the servos in a specific position, adjust one tolerance or another, etc.

So, to help me with these tasks, I started experimenting with the KORG nanoKontrol 2 since it has 8 faders and 8 knobs. It would always be in the corner of the desk, and every time I needed to move a servo one way or another, I could just do it directly on the nanoKontrol.

To make it easier to remember which fader controls which servo, I could simply label each one with an ABC or 123. But I thought it might be more fun if I designed my own knobs and faders and printed each one in a different color. That way I could differentiate them more easily, and it would also make the nanoKontrol more fun.

![]({static}/images/Pasted%20image%2020260516184427.png)

I made each channel a color that's easy to associate in the code: `red`, `orange`, `yellow`. But I avoided using undertones to avoid confusion, for example, having an `orange` and a `dark-orange`. You can go further with this idea of ​​"labeling" with colors and have, for example, two channels that share the same color (`blue-a`, `blue-b`) if they belong to the same context in the application.

![]({static}/images/Pasted%20image%2020260516151026.png)

I've already printed several of these in various colors so I can switch them around according to what makes sense in the project. It's made things much easier.

Download the knobs and faders I made:

- [GitHub](https://github.com/EEmery/assets-repository/tree/main/models/KORG%20nanoKontrol%202%20Knobs%20and%20Faders)
- [Printables](https://www.printables.com/model/1723262-korg-nanokontrol-2-alternative-knobs-and-faders/files)
