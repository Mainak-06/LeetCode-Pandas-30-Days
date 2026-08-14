import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
   own_views= views[views['author_id'] == views['viewer_id']]
   unique_authors = own_views[['author_id']].drop_duplicates()
   sorted_authors = unique_authors.sort_values(by='author_id')
   result = sorted_authors.rename(columns={'author_id':'id'})
   return result