"""
Thank you for taking the time to explore options at Nike. A core part of roles on the Search Sciences team will be
coding. The most relaxing and equitable way we could think of including coding in the interview pipeline was a take
home exercise.

You'll implement a modified nDCG metric based on the well laid out blog post kindly written by Hugh Williams:
https://tech.ebayinc.com/engineering/measuring-search-relevance/ We'll adjust the weights of how valuable a search
result was based on whether or not a searcher clicked, added to cart, or purchased an item. Please use the skeleton
functions and explanations to provide the code for calculating each stage of nDCG. Each stage should be straight forward
with a potential solution of less than 10 lines, but pay attention to accuracy of the metric calculation. Examples of
expected input and output are provided.

Best practices that will make it easier for a rapid response from us:
 - Please modify the filename to include your name
 - Please return a modified .py file, not a notebook
 - Please do NOT modify the function signatures

This is not a timed exercise and does not need to be completed all at once. At a relaxed pace, the expected time
involved is less than 60 minutes.

For bugs, questions, and feedback on the coding exercise please reach out to june.andrews@nike.com thank you!
"""

"""
Implement a modified version of the nDCG metric described here:
https://tech.ebayinc.com/engineering/measuring-search-relevance/

We'll follow along with the blog post creating helper functions for each stage of the calculation. The modification
from the blog post will be a custom set of weights for different user actions. Instead of:

  "we give a 0 score for an irrelevant result, 1 for a partially relevant, 2 for relevant, and 3 for perfect"

Use the scores:

   0 score for products with no clicks
   1 score for products with a click
   3 score for products with an add to cart
   10 score for products with a purchase (if purchased, ignore any other actions, take the highest possible score)

"""


class CustomNDCGMetrics():

    def calculate_gain(self, search_ranking, products_clicked, products_added_to_cart, products_purchased):
        """Calculates the gain for this search ranking given the actions taken on products.

        Args:
          search_ranking (list of product_ids): an ordered list of the product_ids returned for the search
          products_clicked (list of product_ids): list of product_ids that were clicked on
          products_added_to_cart (list of product_ids): list of product_ids that were added to cart from search
          products_purchased (list of product_ids): list of product_ids that were purchased from search

        Returns:
          (list): the gain for each search position

        (TODO 1a) - update the scores (3, 2, 1, 0) scores used below to the (10, 3, 1, 0) scores as outlined above

        Ex Input:
          search_ranking = ["shoe_1", "shoe_2", "shoe_3"]
          products_clicked = ["shoe_2", "shoe_3"]
          products_added_to_cart = ["shoe_3"]
          products_purchased = ["shoe_3"]

        Ex Output:
          Gain = [0, 1, 10]
        """
        gain = [0 for i in range(len(search_ranking))]

        for (rank, product) in enumerate(search_ranking):
            # TODO update score for the custom weighting outlined in the comments above
            score = 0

            gain[rank] = score

        return gain

    def calculate_cumulative_gain(self, search_ranking, products_clicked, products_added_to_cart, products_purchased):
        """Calculates the cumulative gain for this search ranking given the actions taken on products.

        Args:
          search_ranking (list of product_ids): an ordered list of the product_ids returned for the search
          products_clicked (list of product_ids): list of product_ids that were clicked on
          products_added_to_cart (list of product_ids): list of product_ids that were added to cart from search
          products_purchased (list of product_ids): list of product_ids that were purchased from search

        Returns:
          (list): the cumulative gain for each search position

        Ex Input:
          search_ranking = ["shoe_1", "shoe_2", "shoe_3"]
          products_clicked = ["shoe_2", "shoe_3"]
          products_added_to_cart = ["shoe_3"]
          products_purchased = ["shoe_3"]

        Ex Intermediate Steps:
          Gain = [0, 1, 10]

        Ex Output:
          Cumulative Gain = [0, 1, 11]
        """
        gain = self.calculate_gain(search_ranking, products_clicked, products_added_to_cart, products_purchased)
        cumulative_gain = [0.0 for i in gain]  # TODO calculate cumulative gain
        return cumulative_gain

    def calculate_discounted_cumulative_gain(self,
                                             search_ranking,
                                             products_clicked,
                                             products_added_to_cart,
                                             products_purchased):
        """Calculates the discounted cumulative gain for this search ranking given the actions taken on products.

        Args:
          search_ranking (list of product_ids): an ordered list of the product_ids returned for the search
          products_clicked (list of product_ids): list of product_ids that were clicked on
          products_added_to_cart (list of product_ids): list of product_ids that were added to cart from search
          products_purchased (list of product_ids): list of product_ids that were purchased from search

        Returns:
          (list): the discounted cumulative gain for each search position

        Ex Input:
          search_ranking = ["shoe_1", "shoe_2", "shoe_3"]
          products_clicked = ["shoe_2", "shoe_3"]
          products_added_to_cart = ["shoe_3"]
          products_purchased = ["shoe_3"]

        Ex Intermediate Steps:
          Gain = [0, 1, 10]
          Cumulative Gain = [0, 1, 11]
          Discounted Gain = [0/1, 1/2, 10/3]

        Ex Output:
          Discounted Cumulative Gain (DCG) = [0, 0.5, 3.83]

        """
        gain = self.calculate_gain(search_ranking, products_clicked, products_added_to_cart, products_purchased)
        discounted_cumulative_gain = [0.0 for i in gain]  # TODO calculate discounted_cumulative_gain
        return discounted_cumulative_gain

    def calculate_normalized_discounted_cumulative_gain(self,
                                                        search_ranking,
                                                        products_clicked,
                                                        products_added_to_cart,
                                                        products_purchased):
        """Calculates the normalized discounted cumulative gain for this search ranking given the actions taken on
        products.

        Args:
          search_ranking (list of product_ids): an ordered list of the product_ids returned for the search
          products_clicked (list of product_ids): list of product_ids that were clicked on
          products_added_to_cart (list of product_ids): list of product_ids that were added to cart from search
          products_purchased (list of product_ids): list of product_ids that were purchased from search

        Returns:
          (list): the discounted cumulative gain for each search position

        Ex Input:
          search_ranking = ["shoe_1", "shoe_2", "shoe_3"]
          products_clicked = ["shoe_2", "shoe_3"]
          products_added_to_cart = ["shoe_3"]
          products_purchased = ["shoe_3"]

        Ex Intermediate Steps:
          Gain = [0, 1, 10]
          Cumulative Gain = [0, 1, 11]
          Discounted Gain = [0/1, 1/2, 10/3]
          Discounted Cumulative Gain (DCG) = [0, 0.5, 3.83]
          Ideal Discounted Gain = [10 / 1, 1 / 2, 0 / 3]
          Ideal Discounted Cumulative Gain (iDCG) = [10, 10.5, 10.5]

        Ex Output:
          Normalized Discounted Cumulative Gain (nDCG) = [0 / 10, 0.5 / 10.5, 3.83 / 10.5]
        """
        discounted_cumulative_gain = self.calculate_discounted_cumulative_gain(
            search_ranking,
            products_clicked,
            products_added_to_cart,
            products_purchased
        )

        # Calculate the ideal gain
        ideal_discounted_cumulative_gain = [1.0 for i in discounted_cumulative_gain]

        normalized_dcg = [
            actual / ideal
            for (actual, ideal) in zip(discounted_cumulative_gain, ideal_discounted_cumulative_gain)
        ]
        return normalized_dcg
