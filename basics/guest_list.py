# make a list of at least 3 guest lists for dinner
guests = ['cleopatra','catherine the great','napoleon']

# print a message to each person, inviting them to dinner
invitee = 'cleopatra'
guests.remove(invitee)

print(f"{invitee.title()}, your presence is humbly requested for dinner. Will you attend?")

invitee = guests.pop(0) 
print(f"{invitee.title()}, I would love to have you visit for dinner. Will you be able to make it?")

invitee = guests.pop()
print(f"{invitee.title()}, humbly requesting your presence at dinner.")

# turns out someone can't make it. update list and print new invites
guests = ['cleopatra','catherine the great','napoleon']

no_rsvp = 'napoleon'
guests.remove(no_rsvp)

print(f"{no_rsvp.title()} is unable to make dinner. Who can I invite?")

new_guest = 'anne of cleves'
guests.append(new_guest)

invite = guests.pop()
print(f"{invite.title()}, I would love it if you were able to attend my dinner party!")