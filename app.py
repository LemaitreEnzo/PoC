import requests

base_url = "http://localhost"
# /api/v1/posts
url = f"{base_url}/api/v1/posts/"
data = {
    "title": "Hello Worldh,,x",
    "description": "This is my first post"
}
# Add headers
headers = {
    "Authorization" : "Bearer 5Xj6btki1WWOpdry8np8l5WuaxFs2kNodsYRdYsPFL4fF2b3AfofZJlItvWtKvZp"
}
def create_new_post():
    try:
        # Envoi de la requête POST avec les données
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            # Si la requête est réussie, récupérer les données de la réponse
            post_data = response.json()
            post = {
                'id': post_data.get('id'),
                'title': post_data.get('title'),
                'description': post_data.get('description')
            }
            print("Bonne requête :", response.status_code, response.reason)
            return post
        else:
            print("Erreur lors de la requête :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     new_post = create_new_post()
#     if new_post:
#         print("Nouveau post créé avec succès : " )
#         print(new_post)
#     else:
#         print("La création du nouveau post a échoué.")
        
        
def get_posts():
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            # Si la requête est réussie, récupérer les données de la réponse
            posts_data = response.json()
            posts = []
            for post_data in posts_data:
                post = {
                    'id': post_data.get('id'),
                    'title': post_data.get('title'),
                    'description': post_data.get('description')
                }
                posts.append(post)
            print("Bonne requête :", response.status_code, response.reason)
            return posts
        else:
            print("Erreur lors de la requête :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     all_posts = get_posts()
#     if all_posts:
#         print("Liste de tous les posts :")
#         for post in all_posts:
#             print(post)
#     else:
#         print("La récupération des posts a échoué.")



def edit_post(post_id, updated_data):
    try:
        url = f"{base_url}/api/v1/posts/{post_id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            post_data = response.json()
            
            post_data.update(updated_data)
            response = requests.put(url, json=post_data, headers=headers)
            
            if response.status_code == 200 or response.status_code == 201:
                print("Bonne requête :", response.status_code, response.reason)
                return post_data
            else:
                print("Erreur lors de la requête PUT :", response.status_code, response.reason)
                return None
        else:
            print("Erreur lors de la requête GET :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     post_id = 6
#     updated_data = {
#         "title": "Nouveau titre",
#         "description": "Nouvelle description"
#     }
#     edited_post = edit_post(post_id, updated_data)
#     if edited_post:
#         print("Données du post édité :", edited_post)
#     else:
#         print("Impossible d'éditer le post.")


def vote_post(post_id):
    try:
        url = f"{base_url}/api/v1/posts/{post_id}/votes"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            response = requests.post(url, json=data, headers=headers)
            
            if response.status_code == 200 or response.status_code == 201:
                print("Vote accepté :", response.status_code, response.reason)
            else:
                print("Erreur lors de la requête PUT :", response.status_code, response.reason)
                return None
        else:
            print("Erreur lors de la requête GET :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None
    
# if __name__ == "__main__":
#     post_id = 5
#     vote = vote_post(post_id) 

def delete_post(post_id):
    try:
        url = f"{base_url}/api/v1/posts/{post_id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            post_data = response.json()
            response = requests.delete(url, json=post_data, headers=headers)
            
            if response.status_code == 200 or response.status_code == 201:
                print("Supprimé :", response.status_code, response.reason)
            else:
                print("Erreur lors de la requête DELETE :", response.status_code, response.reason)
                return None
        else:
            print("Erreur lors de la requête GET :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     post_id = 7
#     del_post = delete_post(post_id)






# CRUD commentaire sur un post


def add_comment(post_id, comment_data):
    try:
        url = f"{base_url}/api/v1/posts/{post_id}/comments"
        response = requests.post(url, json=comment_data, headers=headers)
        
        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            print("Erreur lors de la requête POST :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     post_id = 12
#     comment_data = {
#         "content": "Ceci est un commentaire pas ouf"
#     }
#     new_comment = add_comment(post_id, comment_data)
#     if new_comment:
#         print("Nouveau commentaire ajouté :")
#         print(new_comment)
#     else:
#         print("Erreur lors de l'ajout du commentaire.")


def get_comments(postid):
    try:
        url = f"{base_url}/api/v1/posts/{postid}/comments"
        response = requests.get(url, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            # Si la requête est réussie, récupérer les données de la réponse
            comments_data = response.json()
            return comments_data
        else:
            print("Erreur lors de la requête :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     postid = 12
#     all_comments = get_comments(postid)
#     if all_comments:
#         print(f"Liste de tous les commentaires du post n°{postid} ")
#         for comment in all_comments:
#             print(comment)
#     else:
#         print("Impossible d'afficher les commentaires.")

def get_comment(post_id, comment_id):
    try:
        url = f"{base_url}/api/v1/posts/{post_id}/comments/{comment_id}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            # Si la requête est réussie, récupérer les données de la réponse
            comments_data = response.json()
            print("Bonne requête :", response.status_code, response.reason)
            return comments_data
        else:
            print("Erreur lors de la requête :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     post_id = 12
#     comment_id = 7
#     comment = get_comment(post_id, comment_id)
#     if comment is not None:
#         print("Commentaire récupéré : ")
#         print("- ", comment.get('content'))
#     else:
#         print("Impossible d'afficher les commentaires.")

def edit_post(post_id, comment_id,updated_data):
    try:
        url = f"{base_url}/api/v1/posts/{post_id}/comments/{comment_id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            post_data = response.json()
            
            post_data.update(updated_data)
            response = requests.put(url, json=post_data, headers=headers)
            
            if response.status_code == 200 or response.status_code == 201:
                return post_data
            else:
                print("Erreur lors de la requête PUT :", response.status_code, response.reason)
                return None
        else:
            print("Erreur lors de la requête GET :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     post_id = 12
#     comment_id = 7
#     updated_data = {
#         "content": "Nouvelle description"
#     }
#     edited_post = edit_post(post_id, comment_id, updated_data)
#     if edited_post:
#         print("Post édité")
#     else:
#         print("Impossible d'éditer le post.")

def delete_comment(post_id, comment_id):
    try:
        url = f"{base_url}/api/v1/posts/{post_id}/comments/{comment_id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            post_data = response.json()
            response = requests.delete(url, json=post_data, headers=headers)
            
            if response.status_code == 200 or response.status_code == 201:
                print("Supprimé :", response.status_code, response.reason)
            else:
                print("Erreur lors de la requête DELETE :", response.status_code, response.reason)
                return None
        else:
            print("Erreur lors de la requête GET :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None   
    
    
# if __name__ == "__main__":
#     post_id = 12
#     comment_id = 6
#     del_comment = delete_comment(post_id, comment_id)




# USERS

def get_users():
    try:
        url = f"{base_url}/api/v1/users"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            users_data = response.json()
            return users_data
        else:
            print("Erreur lors de la requête :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

def create_user(user_data):
    try:
        url = f"{base_url}/api/v1/users"
        response = requests.post(url, json=user_data, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            print("Erreur lors de la requête POST :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

if __name__ == "__main__":
    all_users = get_users()
    if all_users:
        print("Liste de tous les utilisateurs :")
        for post in all_users:
            print(post)
    else:
        print("La récupération des utilisateurs a échoué.")


def create_user(user_data):
    try:
        url = f"{base_url}/api/v1/users"
        response = requests.post(url, json=user_data, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            data = response.json()
            user = {
                'id' : data.get('id'),
                'name' : user_data.get('name'),
                'email' : user_data.get('email')
            }
            return user
        else:
            print("Erreur lors de la requête POST :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None

# if __name__ == "__main__":
#     user_data = {
#     'name' : 'John Doeoi',
#     'email' : 'john_doeoi@gmail.com',
# }
#     new_user = create_user(user_data)
#     if new_user:
#         print("Nouvel utilisateur créé avec succès : " )
#         print(new_user)
#     else:
#         print("La création du nouvel utilisateur a échoué.")



# TAGS









# INVITATIONS

def send_a_sample():
    try:
        url = f"{base_url}/api/v1/invitations/sample"
        response = requests.post(url, headers=headers)

        if response.status_code == 200 or response.status_code == 201:
            pass
        else:
            print("Erreur lors de la requête :", response.status_code, response.reason)
            return None
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête :", e)
        return None    