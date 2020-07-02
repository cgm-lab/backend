from uuid import uuid4
from feedgen.feed import FeedGenerator


def create_feed():
    # date, speaker, papers
    fg = FeedGenerator()
    fg.id(uuid4())
    fg.title("Seminar Schedule")
    fg.description("See ")
    fg.link(href="https://cgm.cs.ntust.edu.tw/seminar/")
    fg.language("en")

    fe = fg.add_entry()
    fe.id()
    print( fg.atom_str(pretty=True) )
    print( fg.rss_str(pretty=True) )

create_feed()