# RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequestBid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **int** | Vendor responsible for bid | 
**lump_sum_amount** | **float** | Lump sum (overall) amount | [optional] 
**bidder_comments** | **str** | Comments | [optional] 
**is_bidder_committed** | **bool** | Bidder committed | [optional] 
**submitted** | **bool** | Vendor submitted Bid | [optional] [default to False]
**recipient_ids** | **List[int]** | Array of Login IDs to add as recipients | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request_bid import RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequestBid

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequestBid from a JSON string
rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request_bid_instance = RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequestBid.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequestBid.to_json())

# convert the object into a dict
rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request_bid_dict = rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request_bid_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequestBid from a dict
rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request_bid_from_dict = RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsPostRequestBid.from_dict(rest_v10_projects_project_id_bid_packages_bid_package_id_bids_post_request_bid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


