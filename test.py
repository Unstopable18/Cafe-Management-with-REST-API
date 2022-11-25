import hashlib
a_string = 'vaishnavi'
hashed_string = hashlib.sha256(args.get("password").encode('utf-8')).hexdigest()
print(hashed_string=='74f5b68b814f869cc954ab8218abc3fde0dc74ab8b2527268cb610abb1afe36f')