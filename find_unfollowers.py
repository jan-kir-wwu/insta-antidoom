import argparse
import instaloader


def parse_args():
    parser = argparse.ArgumentParser(description="Find accounts you follow that don't follow you back")
    parser.add_argument('-u', '--username', required=True, help='Your Instagram username')
    parser.add_argument('-p', '--password', help='Your Instagram password (or set INSTAGRAM_PASS env variable)')
    return parser.parse_args()


def main():
    args = parse_args()
    password = args.password
    if password is None:
        import os
        password = os.getenv('INSTAGRAM_PASS')
        if password is None:
            raise SystemExit('Password not provided via argument or INSTAGRAM_PASS env variable')

    L = instaloader.Instaloader()
    try:
        L.login(args.username, password)
    except Exception as e:
        raise SystemExit(f'Login failed: {e}')

    profile = instaloader.Profile.from_username(L.context, args.username)

    followers = {follower.username for follower in profile.get_followers()}
    followees = {followee.username for followee in profile.get_followees()}

    not_following_back = sorted(followees - followers)

    print('\n'.join(not_following_back))


if __name__ == '__main__':
    main()
