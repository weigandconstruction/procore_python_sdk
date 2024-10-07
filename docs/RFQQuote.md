# RFQQuote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**commitment_quote_number** | **str** | Commitment quote number | [optional] 
**cost** | **float** | Cost | [optional] 
**schedule_impact** | **int** | Schedule impact | [optional] 
**description** | **str** | Description | [optional] 
**request_for_quote_id** | **int** | RFQ ID | [optional] 
**attachments_count** | **int** | Attachments count | [optional] 
**import_origin_id** | **str** | Import origin ID | [optional] 
**created_by_id** | **int** | Created by ID — DEPRECATED, please use \&quot;created_by\&quot; instead | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**prostore_file_ids** | **List[int]** | Array of prostore file ids | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RFQQuoteAttachmentsInner]**](RFQQuoteAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rfq_quote import RFQQuote

# TODO update the JSON string below
json = "{}"
# create an instance of RFQQuote from a JSON string
rfq_quote_instance = RFQQuote.from_json(json)
# print the JSON string representation of the object
print(RFQQuote.to_json())

# convert the object into a dict
rfq_quote_dict = rfq_quote_instance.to_dict()
# create an instance of RFQQuote from a dict
rfq_quote_from_dict = RFQQuote.from_dict(rfq_quote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


