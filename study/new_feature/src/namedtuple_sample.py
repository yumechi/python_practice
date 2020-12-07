from typing import NamedTuple
from dataclasses import dataclass


@dataclass
class Idol:
    name: str
    profile: str


class Live(NamedTuple):
    title: str
    member: list[Idol]

    def summary(self) -> str:
        return "title: {title}\nmember: \n  - {member_name}".format(
            title=self.title,
            member_name="\n  - ".join([m.name for m in self.member]),
        )


if __name__ == "__main__":
    raara = Idol(name="raara", profile="kashikoma Idol")
    mirei = Idol(name="mirei", profile="pripri Idol")
    today_live = Live(title="Bold SUMMER ADVENTURE", member=[raara, mirei])
    print(today_live.summary())
