# RestV10CompaniesCompanyIdBidsIdPatchRequestBid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments_attributes** | [**List[RestV10CompaniesCompanyIdBidsIdPatchRequestBidAttachmentsAttributesInner]**](RestV10CompaniesCompanyIdBidsIdPatchRequestBidAttachmentsAttributesInner.md) |  | [optional] 
**bidder_comments** | **str** | Comments | [optional] 
**bidder_exclusion** | **str** | Exclusions | [optional] 
**bidder_id** | **float** | Bidder Login ID | [optional] 
**bidder_inclusion** | **str** | Inclusions | [optional] 
**bid_items_attributes** | [**List[RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner]**](RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner.md) |  | [optional] 
**is_bidder_committed** | **bool** | Bidder committed | [optional] 
**lump_sum_amount** | **float** | Lump sum (overall) amount | [optional] 
**submitted** | **bool** | Vendor submitted Bid | [optional] [default to False]
**uploads** | [**List[RestV10CompaniesCompanyIdBidsIdPatchRequestBidUploadsInner]**](RestV10CompaniesCompanyIdBidsIdPatchRequestBidUploadsInner.md) |  | [optional] 
**bid_items_to_delete** | **List[int]** | IDs of Bid Items that need to be deleted | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bids_id_patch_request_bid import RestV10CompaniesCompanyIdBidsIdPatchRequestBid

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidsIdPatchRequestBid from a JSON string
rest_v10_companies_company_id_bids_id_patch_request_bid_instance = RestV10CompaniesCompanyIdBidsIdPatchRequestBid.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidsIdPatchRequestBid.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bids_id_patch_request_bid_dict = rest_v10_companies_company_id_bids_id_patch_request_bid_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidsIdPatchRequestBid from a dict
rest_v10_companies_company_id_bids_id_patch_request_bid_from_dict = RestV10CompaniesCompanyIdBidsIdPatchRequestBid.from_dict(rest_v10_companies_company_id_bids_id_patch_request_bid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


