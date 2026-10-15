import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    results = []
    for a in anon_df.itertuples():
        matches = []
        for b in aux_df.itertuples():
            if(a.age == b.age and a.zip3 == b.zip3 and a.gender == b.gender):
                matches.append(b.name)
        if len(matches) == 1:
            results.append({"anon_id": a.anon_id, "matched_name": matches[0]})

    return pd.DataFrame(results, columns=["anon_id", "matched_name" ])

def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return len(matches_df)/len(anon_df)
