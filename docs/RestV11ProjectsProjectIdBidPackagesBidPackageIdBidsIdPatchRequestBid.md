# RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lump_sum_amount** | **float** | Lump sum (overall) amount | [optional] 
**bidder_comments** | **str** | Comments | [optional] 
**bidder_inclusion** | **str** | Inclusions | [optional] 
**bidder_exclusion** | **str** | Exclusions | [optional] 
**bid_status** | **str** | This status is combination of the &#x60;invitation_last_sent_at&#x60;, &#x60;is_bidder_committed&#x60;, &#x60;submitted&#x60;, &amp; &#x60;awarded&#x60; values. The &#x60;not_invited&#x60;  status is the same as &#x60;invitation_last_sent_at&#x60; being null,     &#x60;is_bidder_committed&#x60; being null,  &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;undecided&#x60;    status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being null,  &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;will_not_bid&#x60; status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being false, &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;will_bid&#x60;     status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being true,  &#x60;submitted&#x60; being false, &amp; &#x60;awarded&#x60; not being true. The &#x60;submitted&#x60;    status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being true,  &#x60;submitted&#x60; being true,  &amp; &#x60;awarded&#x60; not being true. The &#x60;awarded&#x60;      status is the same as &#x60;invitation_last_sent_at&#x60; not being null, &#x60;is_bidder_committed&#x60; being true,  &#x60;submitted&#x60; being true,  &amp; &#x60;awarded&#x60; being true.  | [optional] 
**is_bidder_committed** | **bool** | Bidder committed | [optional] 
**submitted** | **bool** | Vendor submitted Bid | [optional] [default to False]
**prostore_file_ids** | **List[int]** | Array of Prostore File IDs for attachments | [optional] 
**recipient_ids** | **List[int]** | Array of Login IDs to add as recipients | [optional] 
**bid_items** | [**List[RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBidBidItemsInner]**](RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBidBidItemsInner.md) | Bid Items for a Bid | [optional] 
**bid_items_to_delete** | **List[int]** | IDs of Bid Items that need to be deleted | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid import RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid from a JSON string
rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_instance = RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid.to_json())

# convert the object into a dict
rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_dict = rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid from a dict
rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_from_dict = RestV11ProjectsProjectIdBidPackagesBidPackageIdBidsIdPatchRequestBid.from_dict(rest_v11_projects_project_id_bid_packages_bid_package_id_bids_id_patch_request_bid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


