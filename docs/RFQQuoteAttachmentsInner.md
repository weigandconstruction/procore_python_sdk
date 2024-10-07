# RFQQuoteAttachmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 

## Example

```python
from procore_sdk.models.rfq_quote_attachments_inner import RFQQuoteAttachmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RFQQuoteAttachmentsInner from a JSON string
rfq_quote_attachments_inner_instance = RFQQuoteAttachmentsInner.from_json(json)
# print the JSON string representation of the object
print(RFQQuoteAttachmentsInner.to_json())

# convert the object into a dict
rfq_quote_attachments_inner_dict = rfq_quote_attachments_inner_instance.to_dict()
# create an instance of RFQQuoteAttachmentsInner from a dict
rfq_quote_attachments_inner_from_dict = RFQQuoteAttachmentsInner.from_dict(rfq_quote_attachments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


