# RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lump_sum_amount** | **float** | Lump sum (overall) amount | [optional] 
**bidder_comments** | **str** | Comments | [optional] 
**bidder_inclusion** | **str** | Inclusions | [optional] 
**bidder_exclusion** | **str** | Exclusions | [optional] 
**is_bidder_committed** | **bool** | Bidder committed | [optional] 
**submitted** | **bool** | Vendor submitted Bid | [optional] [default to False]
**recipient_ids** | **List[int]** | Array of Login IDs to add as recipients | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid import RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid from a JSON string
rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_instance = RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid.to_json())

# convert the object into a dict
rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_dict = rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid from a dict
rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_from_dict = RestV10ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid.from_dict(rest_v10_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


