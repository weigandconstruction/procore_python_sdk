# RFQQuote1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitment_quote_number** | **str** | Commitment quote number | [optional] 
**cost** | **float** | Cost | [optional] 
**description** | **str** | Description | [optional] 
**schedule_impact** | **int** | Schedule impact | [optional] 

## Example

```python
from procore_sdk.models.rfq_quote1 import RFQQuote1

# TODO update the JSON string below
json = "{}"
# create an instance of RFQQuote1 from a JSON string
rfq_quote1_instance = RFQQuote1.from_json(json)
# print the JSON string representation of the object
print(RFQQuote1.to_json())

# convert the object into a dict
rfq_quote1_dict = rfq_quote1_instance.to_dict()
# create an instance of RFQQuote1 from a dict
rfq_quote1_from_dict = RFQQuote1.from_dict(rfq_quote1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


