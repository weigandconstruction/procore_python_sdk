# RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_in_cents** | **float** | Amount In Cents | [optional] 
**bid_form_item_id** | **float** | Bid Form Item ID | [optional] 
**cost_code_id** | **float** | Cost Code ID | [optional] 
**id** | **float** | ID | [optional] 
**included** | **bool** | Incldued | [optional] 
**quantity** | **str** | Quantity | [optional] 
**unit_cost** | **str** | Unit Cost | [optional] 
**uom** | **str** | Unit of Measure | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_companies_company_id_bids_id_patch_request_bid_bid_items_attributes_inner import RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner from a JSON string
rest_v10_companies_company_id_bids_id_patch_request_bid_bid_items_attributes_inner_instance = RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner.to_json())

# convert the object into a dict
rest_v10_companies_company_id_bids_id_patch_request_bid_bid_items_attributes_inner_dict = rest_v10_companies_company_id_bids_id_patch_request_bid_bid_items_attributes_inner_instance.to_dict()
# create an instance of RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner from a dict
rest_v10_companies_company_id_bids_id_patch_request_bid_bid_items_attributes_inner_from_dict = RestV10CompaniesCompanyIdBidsIdPatchRequestBidBidItemsAttributesInner.from_dict(rest_v10_companies_company_id_bids_id_patch_request_bid_bid_items_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


